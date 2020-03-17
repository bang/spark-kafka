# Spark-kafka references

 Document with references to build spark-kafka projects using **pySpark**



## Requirements

First of all read this [document](file://Spark StructuredStreaming - The basics.md)

### Version of things

 The 'primordial' environment was built using:

 * Spark 2.4.4

 * Scala 2.11.12

 * Apache Kafka 2.11-2.4.0 (Scala version - Kafka build version)

 * Hadoop 2.8.5

 For convenience I built this on docker - [ramtricks/hadoop-bootstrap](https://hub.docker.com/repository/docker/ramtricks/hadoop-bootstrap)



### Java libs

 Is necessary to import two *.jar* files together on your Spark-kafka in order to load. Versions matters(as everything wrote in Java and Scala). For convenience, I've separated the right versions for you. But, you can find all of this on [maven repository](https://maven.org) 

* spark-sql-kafka-0-10_2.11-2.4.4.jar
* spark-streaming-kafka-assembly_2.11-1.6.3.jar
* kafka-clients-2.4.0.jar



## Code

Just *pySpark* for now. Sorry!





**Import**

```python
import pyspark
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import expr
import json
```



**SparkSession**

```python
spark = SparkSession.builder.appName('kafka-test'
         ).config('spark.jars',"jars/spark-sql-kafka-0-10_2.11-2.4.4.jar" +
                              ",jars/spark-streaming-kafka-assembly_2.11-1.6.3.jar" 
         ).config('spark.driver.extraClassPath','jars/kafka-clients-2.4.0.jar'
         ).getOrCreate()
```

For reasons I can't explain yet, is necessary load *kafka-clients-2.4.0.jar* separated using *spark.driver.extraClassPath* parameter inside the configuration.



**Establishing streaming**

```python
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
```

You must implement *readStream* **AND** *writeStream*. This is a mandatory feature.

On **readStream** I'm just getting text data from a topic called *test*, and selecting two columns from the resultant dataframe. Yes! you can use *pyspark.sql*

On **writeStream**, for simplicity I choose to write on 'memory' that is one of many possible ways to write 