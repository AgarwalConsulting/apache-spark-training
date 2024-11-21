import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import scala.concurrent.duration._

object PublicationInfluenceAnalysis {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder
      .appName("Publication Influence Analysis")
      .getOrCreate()



    val df = spark.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("data_sets/critic_reviews.csv")

    val dfWithInts = df.withColumn("isFreshInt", col("isFresh").cast("int"))
      .withColumn("isRottenInt", col("isRotten").cast("int"))

    // Perform aggregation
    val publicationAnalysis = dfWithInts.groupBy("publicationName").agg(
      sum("isFreshInt").alias("fresh_reviews"),
      sum("isRottenInt").alias("rotten_reviews"),
      count("reviewId").alias("total_reviews"),
      avg("originalScore").alias("average_original_score")
    )

    val publicationAnalysisWithProportions = publicationAnalysis.withColumn(
      "fresh_proportion", col("fresh_reviews") / col("total_reviews")
    ).withColumn(
      "rotten_proportion", col("rotten_reviews") / col("total_reviews")
    )

    // Save the results to a CSV file
    val outputPath = "output/publication_analysis_results.csv"
    publicationAnalysisWithProportions.coalesce(1)
      .write.option("header", "true")
      .mode("overwrite")
      .csv(outputPath)

    df.explain(true)
    Thread.sleep(100000 * 1000)

    spark.stop()
  }
}
