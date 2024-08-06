from pyspark.sql import SparkSession

import time

def main():
    spark = SparkSession.builder \
        .appName("Sum of Multiples") \
        .getOrCreate()

    range_rdd = spark.sparkContext.parallelize(range(1, 1001))
    filtered_rdd = range_rdd.filter(lambda x: x % 3 == 0 or x % 5 == 0)
    sum_of_multiples = filtered_rdd.sum()

    print(sum_of_multiples)

    time.sleep(10000)

    spark.stop()

if __name__ == "__main__":
    main()
