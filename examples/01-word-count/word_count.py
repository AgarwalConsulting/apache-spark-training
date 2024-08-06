sc = SparkContext.getOrCreate()

input_file = "/Users/gaurav/Developer/Training/Spark/README.md"
text_rdd = sc.textFile(input_file)

word_counts = text_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

output_dir = "output"
word_counts.saveAsTextFile(output_dir)
