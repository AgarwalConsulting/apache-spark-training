from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = SparkSession.builder \
    .appName("simple-python-starters") \
    .getOrCreate()


df = spark.read.csv("examples/simple-python-starters/Airline_Delay_Cause.csv", header=True, inferSchema=True)

df.write.mode("overwrite").parquet("output/Airline_Delay_Cause.parquet")


parquet_df = spark.read.parquet("output/Airline_Delay_Cause.parquet")

carrier_grouped_df = parquet_df.groupBy('carrier_name').agg(
    F.sum('arr_flights').alias('total_flights'),
    F.sum('arr_del15').alias('total_delays')
)

carrier_grouped_df = carrier_grouped_df.withColumn(
    'delay_percentage',
    (F.col('total_delays') / F.col('total_flights')) * 100
)

sorted_carrier_df = carrier_grouped_df.orderBy(F.col('delay_percentage').desc())


sorted_carrier_df.write.mode("overwrite").parquet("output/carrier_delays_percentage.parquet")


spark.stop()
