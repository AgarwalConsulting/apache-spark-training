from pyspark.sql import SparkSession

import time

def main():
    spark = SparkSession.builder \
        .appName("Word Count") \
        .config("dfs.client.read.shortcircuit.skip.checksum", "true") \
        .getOrCreate()

    sc = spark.sparkContext

    input_file = "/app/examples/good_data_sets.md"
    text_rdd = sc.textFile(input_file)

    word_counts = text_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    output_dir = "output"
    word_counts.saveAsTextFile(output_dir)

    print(word_counts)

    time.sleep(10000)

    sc.stop()

if __name__ == "__main__":
    main()
