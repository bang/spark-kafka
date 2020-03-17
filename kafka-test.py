
# coding: utf-8

# In[1]:


import pyspark
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import expr
# import json
#from pyspark.sql.functions import from_json, col, struct
#from confluent_kafka.avro.serializer.message_serializer import MessageSerializer
#from confluent_kafka.avro.cached_schema_registry_client import CachedSchemaRegistryClient
#from pyspark.sql.column import Column, _to_java_column


# In[4]:
#).config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.0"
jars = "/home/hduser/Projects/kafka/jars"
spark = SparkSession.builder.appName('kafka-test'
         ).config('spark.jars',"jars/spark-sql-kafka-0-10_2.11-2.4.4.jar" +
                               ",jars/spark-streaming-kafka-assembly_2.11-1.6.3.jar" 
         ).config('spark.driver.extraClassPath','jars/kafka-clients-2.4.0.jar'
         ).getOrCreate()

df = spark \
  .readStream \
  .format("kafka"
  ).option("kafka.bootstrap.servers", "localhost:9092"
  ).option("subscribe", "test"
  ).load(
  ).select(col('key').cast('string')
             ,col('value').cast('string')
  ).writeStream \
  .outputMode("append"
  ).format("memory"
  ).queryName('outTest'
  ).start()

#.option("partition.assignment.strategy","RoundRobinAssignor") \
  

