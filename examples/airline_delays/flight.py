from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import time


spark = SparkSession.builder \
    .appName("simple-python-starters") \
    .getOrCreate()



df = spark.read.csv("examples/simple-python-starters/Airline_Delay_Cause.csv", header=True, inferSchema=True)


carrier_grouped = df.groupBy('carrier_name').agg(
    F.sum('arr_flights').alias('total_flights'),
    F.sum('arr_del15').alias('total_delays')
)


#delay percentage
d_carrier_grouped = carrier_grouped.withColumn(
    'delay_percentage',
    (carrier_grouped['total_delays'] / carrier_grouped['total_flights']) * 100
)
d_carrier_grouped = d_carrier_grouped.orderBy(F.col('delay_percentage').desc())
d_carrier_grouped.coalesce(1).write.csv('output/carrier_delays_percentage.csv', header=True)


# #carrier delay
# c_carrier_grouped = carrier_grouped.withColumn(
#     'carrier_delay',
#     (df.groupBy('carrier_name').agg(
#     F.sum('carrier_ct').alias('total_carrier_delay'),
#     F.sum('weather_ct').alias('total_weather_delay'),
#     F.sum('nas_ct').alias('total_nas_delay'),
#     F.sum('security_ct').alias('total_security_delay'),
#     F.sum('late_aircraft_ct').alias('total_late_aircraft_delay')
# ))

# )
# c_carrier_grouped = c_carrier_grouped.orderBy(F.col('carrier_delay').desc())
# c_carrier_grouped.coalesce(1).write.csv('output/carrier_delay.csv', header=True)


# #airport groupred
# airport_grouped = df.groupBy('airport').agg(
#     F.sum('arr_flights').alias('total_flights'),
#     F.sum('arr_del15').alias('total_delays')
# )

# #delay percentage
# d_airport_grouped = airport_grouped.withColumn(
#     'delay_percentage',
#     (airport_grouped['total_delays'] / airport_grouped['total_flights']) * 100
# )

# d_airport_grouped = d_airport_grouped.orderBy(F.col('delay_percentage').desc())
# d_airport_grouped.coalesce(1).write.csv('output/airport_delays_percentage.csv', header=True)


# #airport delay
# a_airport_grouped = airport_grouped.withColumn(
#     'airport_delay',
#     (df.groupBy('airport').agg(
#     F.sum('carrier_ct').alias('total_carrier_delay'),
#     F.sum('weather_ct').alias('total_weather_delay'),
#     F.sum('nas_ct').alias('total_nas_delay'),
#     F.sum('security_ct').alias('total_security_delay'),
#     F.sum('late_aircraft_ct').alias('total_late_aircraft_delay')
# ))
# )
# a_airport_grouped = a_airport_grouped.orderBy(F.col('avg_delay').desc())
# a_airport_grouped.coalesce(1).write.csv('output/airport_delay.csv', header=True).mean()


time.sleep(10000)
spark.stop()






# sqlite3 :memory: -cmd '.import -csv Airline_Delay_Cause.csv delays' \
# 'SELECT carrier_name, COUNT(*) AS record_count, sum(arr_del15) AS total_delay, sum(arr_del15) / COUNT(*) FROM delays GROUP BY carrier_name'