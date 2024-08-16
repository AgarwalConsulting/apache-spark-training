from pyspark.sql import SparkSession
import time


spark = SparkSession.builder \
    .appName("Publication Influence Analysis") \
    .getOrCreate()
start_time = time.time()

rdd = spark.read.csv("data_sets/critic_reviews.csv", header=True, inferSchema=True).rdd


def parse_row(row):
    try:
      
        publicationName = row['publicationName']
        isFresh = int(row['isFresh']) if row['isFresh'] is not None else 0
        isRotten = int(row['isRotten']) if row['isRotten'] is not None else 0
        originalScore = float(row['originalScore']) if row['originalScore'] is not None else 0.0
        return (publicationName, isFresh, isRotten, originalScore)
    except ValueError:
       
        return (row['publicationName'], 0, 0, 0.0)

rdd = rdd.map(parse_row)


rdd = rdd.filter(lambda row: row[0] is not None)


def aggregate_data(rdd):
   
    mapped_rdd = rdd.map(lambda row: (
        row[0], 
        (row[1], row[2], 1, row[3])
    ))

 
    reduced_rdd = mapped_rdd.reduceByKey(lambda a, b: (
        a[0] + b[0],  # Sum of fresh reviews
        a[1] + b[1],  # Sum of rotten reviews
        a[2] + b[2],  # Count of reviews
        a[3] + b[3]   # Sum of original scores
    ))

    result_rdd = reduced_rdd.map(lambda row: (
        row[0],  # publicationName
        row[1][0],  # fresh_reviews
        row[1][1],  # rotten_reviews
        row[1][2],  # total_reviews
        row[1][3] / row[1][2] if row[1][2] > 0 else 0.0,  # average_original_score
        row[1][0] / row[1][2] if row[1][2] > 0 else 0.0,  # fresh_proportion
        row[1][1] / row[1][2] if row[1][2] > 0 else 0.0   # rotten_proportion
    ))

    return result_rdd


publication_analysis_rdd = aggregate_data(rdd)


publication_analysis_df = spark.createDataFrame(
    publication_analysis_rdd,
    ["publicationName", "fresh_reviews", "rotten_reviews", "total_reviews", "average_original_score", "fresh_proportion", "rotten_proportion"]
)

output_path = "output/publication_analysis_results.csv"
publication_analysis_df.coalesce(1).write.csv(output_path, header=True, mode="overwrite")

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
time.sleep(100000)
time.sleep(100000)
spark.stop()
