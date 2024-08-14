from pyspark.sql import SparkSession
import time

spark = SparkSession.builder \
    .appName("simple-python-starters") \
    .getOrCreate()

df = spark.read.csv("examples/simple-python-starters/Airline_Delay_Cause.csv", header=True, inferSchema=True)

rdd = df.rdd


def safe_int(value):
    return int(value) if value is not None else 0

carrier_grouped_rdd = rdd.map(lambda x: (
    x['carrier_name'], 
    (safe_int(x['arr_flights']), safe_int(x['arr_del15']))
)).reduceByKey(lambda x, y: (
    x[0] + y[0], 
    x[1] + y[1]
))

d_carrier_grouped_rdd = carrier_grouped_rdd.mapValues(lambda x: (
    x[0], 
    x[1], 
    (x[1] / x[0]) * 100 if x[0] != 0 else 0
))


sorted_d_carrier_grouped_rdd = d_carrier_grouped_rdd.sortBy(lambda x: x[1][2], ascending=False)

header = "carrier_name,total_flights,total_delays,delay_percentage"
output_rdd = sorted_d_carrier_grouped_rdd.map(lambda x: f"{x[0]},{x[1][0]},{x[1][1]},{x[1][2]:.2f}")


output_rdd = spark.sparkContext.parallelize([header]).union(output_rdd)

output_rdd.coalesce(1).saveAsTextFile("output/carrier_delays_percentage_rdd.csv")

time.sleep(10000)
spark.stop()
