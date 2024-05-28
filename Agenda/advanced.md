# Apache Spark on AWS EMR

## Objectives

This advanced outline focuses on leveraging AWS EMR for running and optimizing Spark workloads.

- Data Engineers deep dive into performance optimization techniques, large-scale data processing, and practical comparisons of Scala and Python.

- The hands-on labs ensure participants gain practical experience in setting up, optimizing, and managing Spark on AWS EMR.

## Agenda

### Day 1

- Recap of Spark Architecture
  - Low-level APIs
  - Structured APIs
  - Differences between Spark 2 vs 3

- Scala vs Python
  - Which is better for Apache Spark?
  - Differences in API
  - Quick notes on Spark via Java or SQL

- Introduction to AWS EMR
  - Overview of AWS EMR architecture
  - Key features and components
  - EMR vs. on-premises Spark cluster
    - EMR on EC2 vs EKS

- Setting Up Spark on EMR
  - Launching an EMR cluster
  - Autoscaling policies and configurations
  - Best practices for instance selection
  - Configuring the EMR cluster for performance

- Resource Management and Scheduling on EMR
  - Configuring YARN on EMR
  - Using Instance Groups and Instance Fleets
  - Job scheduling and priority management

- Exercise: Launching and configuring a Spark Cluster on AWS EMR

- Spark Internals
  - Overview of Catalyst optimizer
  - Logical and physical plan
  - Rule-based and cost-based optimization
  - Tungsten execution engine: In-memory computing, binary processing, and cache-aware computation
  - Evaluating Code Generation & Expression Tree nodes

### Day 2

- Advanced DataFrames and Datasets
  - Optimizing DataFrame transformations
  - Type-Safe Processing using Datasets
  - Using Glue Data Catalog with Spark SQL
  - Custom aggregations and UDFs/UDAFs in EMR

- Language Specific Spark
  - Case Classes in Scala
  - PandasAPI for python
  - Running SQL queries on DataFrames

- Performance Tuning and Optimization Techniques
  - Various Joins in Spark & their impact
    - Utilizing AQE
  - Best practices for writing efficient Spark code
  - Serialization formats: Avro, Parquet, ORC
  - Data partitioning and bucketing
    - Custom Partition
  - Cache, Persist and Checkpoint

- Exercise: Monitoring and debugging Spark jobs using CloudWatch and Spark UI

- Memory Management and Tuning
  - Spark's memory model
  - Memory tuning parameters
  - Garbage collection tuning
  - Off-heap storage

- Optimized ETL Pipelines with EMR
  - Building ETL pipelines using Spark on EMR
  - Best practices for data partitioning and bucketing
  - Handling schema evolution with AWS Glue
  - Best Practices to Prevent Shuffling

- Fault Tolerance
  - Reliable Spark Streaming
  - WALs, RDDs, Availability

### Day 3

- Advanced Spark Streaming
  - Structured Streaming vs. DStreams
  - Stateful transformations
  - Exactly-once semantics
  - Watermarking and window operations

- Machine Learning and Graph Processing
  - Performance considerations for MLlib
  - Tuning ML pipelines
  - GraphX optimization techniques

- Exercise: Logistic Regression, Decision Trees

- Efficient Data Storage and Access: Magic Write to S3
  - Using S3 as a data source and sink
  - Optimizing S3 access patterns
  - Introduction to Magic Write for efficient data writes to S3
  - Comparing different file formats (Parquet, ORC, Avro)

- Deployment Best Practices on EMR
  - Continuous integration and deployment for EMR applications
  - Using AWS CodePipeline and CodeDeploy
  - Security best practices for EMR (IAM roles, encryption, etc.)
