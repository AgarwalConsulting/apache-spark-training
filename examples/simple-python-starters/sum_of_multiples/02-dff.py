from pyspark.sql import SparkSession
import time

def main():
    spark = SparkSession.builder \
        .appName("Sum of Multiples") \
        .getOrCreate()
    
    df = spark.createDataFrame([(i,) for i in range(1, 1001)], ["number"])
    filtered_df = df.filter((df.number % 3 == 0) | (df.number % 5 == 0))
    sum_of_multiples = filtered_df.groupBy().sum("number").collect()[0][0]
    print(sum_of_multiples)
    time.sleep(10000)
    spark.stop()

if __name__ == "__main__":
    main()
