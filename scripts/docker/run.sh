#!/usr/bin/env bash

docker run --name spark-job -it --rm -p 14040:4040 -v "$(pwd):/app/" apache/spark /opt/spark/bin/spark-submit /app/examples/simple-python-starters/sum_of_multiples/01-rdd.py
