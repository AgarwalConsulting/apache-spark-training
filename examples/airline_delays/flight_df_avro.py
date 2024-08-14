from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import time

spark = SparkSession.builder \
    .appName("airline-delays-avro") \
    .getOrCreate()

df = spark.read.csv("data_sets/airline/Airline_Delay_Cause.csv", header=True, inferSchema=True)

carrier_grouped_df = df.groupBy('carrier_name').agg(
    F.sum('arr_flights').alias('total_flights'),
    F.sum('arr_del15').alias('total_delays')
)

carrier_grouped_df = carrier_grouped_df.withColumn(
    'delay_percentage',
    (F.col('total_delays') / F.col('total_flights')) * 100
)

sorted_carrier_df = carrier_grouped_df.orderBy(F.col('delay_percentage').desc())


sorted_carrier_df.write.format("avro").save("output/carrier_delays_percentage.avro")

# time.sleep(100000)

spark.stop()
