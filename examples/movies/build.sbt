name := "FilmAnalysis"

version := "1.0"

scalaVersion := "2.12.10" // Make sure this matches the Scala version for Spark

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "3.1.2" % "provided",
  "org.apache.spark" %% "spark-sql" % "3.1.2" % "provided"
)

mainClass in Compile := Some("com.example.Film")
