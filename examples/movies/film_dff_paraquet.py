from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, avg, col
import time

spark = SparkSession.builder \
    .appName("Publication Influence Analysis") \
    .getOrCreate()


df = spark.read.csv("data_sets/critic_reviews.csv", header=True, inferSchema=True)

df = df.withColumn("isFreshInt", col("isFresh").cast("int")) \
       .withColumn("isRottenInt", col("isRotten").cast("int"))

publication_analysis = df.groupBy("publicationName").agg(
    sum("isFreshInt").alias("fresh_reviews"),
    sum("isRottenInt").alias("rotten_reviews"),
    count("reviewId").alias("total_reviews"),
    avg("originalScore").alias("average_original_score")
)

publication_analysis = publication_analysis.withColumn(
    "fresh_proportion", col("fresh_reviews") / col("total_reviews")
).withColumn(
    "rotten_proportion", col("rotten_reviews") / col("total_reviews")
)

output_path = "output/publication_analysis_results.parquet"


publication_analysis.coalesce(1).write.parquet(output_path, mode="overwrite")


time.sleep(100000)
spark.stop()