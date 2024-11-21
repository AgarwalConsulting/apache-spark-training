#!/usr/bin/env bash

rm -rf output

docker run --name spark-job -it --rm -p 14040:4040 -v "$(pwd):/app/" -w /app apache/spark /opt/spark/bin/spark-submit /app/examples/01-word-count/word_count.py

# docker run --name spark-job-1 -it --rm -p 14041:4040 -v "$(pwd):/app/" -w /app apache/spark /opt/spark/bin/spark-submit /app/examples/simple-python-starters/sum_of_multiples/01-rdd.py

docker run --name spark-job -it --rm -p 14040:4040 -v "$(pwd):/app/" -w /app apache/spark /opt/spark/bin/spark-submit --packages org.apache.spark:spark-avro_2.12:3.5.2 --conf spark.driver.extraJavaOptions="-Divy.cache.dir=/tmp -Divy.home=/tmp" /app/examples/airline_delays/flight_df_avro.py


docker run --name spark-job -it --rm -p 14040:4040 -v "$(pwd):/app/" -w /app apache/spark /opt/spark/bin/spark-submit --packages org.apache.spark:spark-avro_2.12:3.5.2 --conf spark.driver.extraJavaOptions="-Divy.cache.dir=/tmp -Divy.home=/tmp" /app/examples/movies/project/film.scala


docker run --name spark-job -it --rm -p 14040:4040 -v "$(pwd):/app/" -w /app apache/spark /opt/spark/bin/spark-submit /app/examples/movies/project/film.scala
