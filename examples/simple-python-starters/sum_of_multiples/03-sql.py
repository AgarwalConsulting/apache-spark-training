from pyspark.sql import SparkSession

import time

def main():
    spark = SparkSession.builder \
        .appName("Sum of Multiples") \
        .getOrCreate()
    df = spark.createDataFrame([(i,) for i in range(1, 1001)], ["number"])
    df.createOrReplaceTempView("numbers")

    result = spark.sql("""
        SELECT SUM(number) as sum_of_multiples
        FROM numbers
        WHERE number % 3 = 0 OR number % 5 = 0
    """)

    sum_of_multiples = result.collect()[0]["sum_of_multiples"]

    print(sum_of_multiples)
    
    time.sleep(10000)

    

if __name__ == "__main__":
    main()
