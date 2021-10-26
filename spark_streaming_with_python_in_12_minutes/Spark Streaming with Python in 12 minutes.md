# Spark Streaming with Python in 12 minutes

[Spark streaming notes](https://www.notion.so/Spark-streaming-notes-8154392e349d40069a0308f5cae7cb1e)

![Untitled](Spark%20Streaming%20with%20Python%20in%2012%20minutes%20fb6bffa9d7b549a5841b4ab32ff1683e/Untitled.png)

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams.

Data can be ingested from many sources like Kafka, Flume, Kinesis, or TCP sockets, and can be processed using complex algorithms expressed with high-level functions like map, reduce, join and window.

![Untitled](Spark%20Streaming%20with%20Python%20in%2012%20minutes%20fb6bffa9d7b549a5841b4ab32ff1683e/Untitled%201.png)

![Untitled](Spark%20Streaming%20with%20Python%20in%2012%20minutes%20fb6bffa9d7b549a5841b4ab32ff1683e/Untitled%202.png)

- Spark has full integration guide to connect to different data sources
- Documentation
- Two options-
    - Spark Streaming-
    - Structured streaming- uses spark session, does spark streaming based on top of spark SQL engine - should be goto

To get an overview on what structured streaming is 

![Untitled](Spark%20Streaming%20with%20Python%20in%2012%20minutes%20fb6bffa9d7b549a5841b4ab32ff1683e/Untitled%203.png)

- Taking data streaming input, separating into batches,every piece of data in datastream is a new row in unbounded table
- Then you can use trigger

![Untitled](Spark%20Streaming%20with%20Python%20in%2012%20minutes%20fb6bffa9d7b549a5841b4ab32ff1683e/Untitled%204.png)

Input Dstreams and Recievers

Python API As of Spark 3.2.0, out of these sources, Kafka and Kinesis are available in the Python API.