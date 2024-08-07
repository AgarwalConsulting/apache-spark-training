from pyspark.sql import SparkSession

import time
spark = SparkSession.builder.appName("Sum of Multiples").getOrCreate()
sc = spark.sparkContext
def fibonacci(n):
    a, b = 1, 2
    fib_sequence = []
    while a < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

fibonacci_rdd = sc.parallelize(fibonacci(int(1e6)))

even_sum = fibonacci_rdd.filter(lambda x: x % 2 == 0).sum()

print(even_sum)
time.sleep(10000)


