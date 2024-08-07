from pyspark.sql import SparkSession

import time

def main():
    spark = SparkSession.builder \
        .appName("Sum of Multiples") \
        .getOrCreate()

    range_rdd = spark.sparkContext.parallelize(range(1, 1001))

    zero_value = 0
    seq = (lambda acc, x: acc + x if x % 3 == 0 or x % 5 == 0 else acc)
    comb = (lambda acc1, acc2: acc1 + acc2)

    sum_of_multiples = range_rdd.aggregate(zero_value, seq, comb)

    print(sum_of_multiples)



    time.sleep(10000)

    

if __name__ == "__main__":
    main()
