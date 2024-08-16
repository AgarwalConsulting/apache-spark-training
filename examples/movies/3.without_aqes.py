from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, avg, broadcast
import time

spark = SparkSession.builder \
    .appName("Optimized Aggregation") \
    .getOrCreate()

spark.conf.set("spark.sql.adaptive.enabled", "false")


df = spark.read.csv("data_sets/critic_reviews.csv", header=True, inferSchema=True)


df = df.withColumn("isFreshInt", col("isFresh").cast("int")) \
       .withColumn("isRottenInt", col("isRotten").cast("int"))

df = df.repartition("publicationName")


aggregated_df = df.groupBy("publicationName").agg(
    sum("isFreshInt").alias("fresh_reviews"),
    sum("isRottenInt").alias("rotten_reviews"),
    count("reviewId").alias("total_reviews"),
    avg("originalScore").alias("average_original_score")
)


result_df = aggregated_df.withColumn(
    "fresh_proportion", col("fresh_reviews") / col("total_reviews")
).withColumn(
    "rotten_proportion", col("rotten_reviews") / col("total_reviews")
)


output_path = "output/optimized_results.csv"
result_df.coalesce(1).write.csv(output_path, header=True, mode="overwrite")

time.sleep(100000)
spark.stop()
