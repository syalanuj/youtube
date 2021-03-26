# Databricks Tutorial

[Databricks documentation](https://docs.databricks.com/)

# Explore Databricks fundamentals

Topics-

- Few pending concepts
- Databricks archtecture
- Demo of the databricks workspace
- Hands on development
- Deployment of jobs

### Data Problem-

A common theme - "Data is the new Oil" Companiess are collecting huge amounts of data, collecting from all sorts of ingestion streams. This data can derive a lot of opportunity for business growth, improvement, iteration. 

Great Philosophy - however there are quite a lot of issues here

- Data not properly ingested
- issues with coordination
- data is not up to date
- Management overhead, if you are dealing with massive amounts of data- massive operation overhead

This Databricks - unified data analytics platform

Core components

![Databricks%20Tutorial%20f4ab85ef14374675b8075ee73a51c22b/Untitled.png](Databricks%20Tutorial%20f4ab85ef14374675b8075ee73a51c22b/Untitled.png)

source from databricks youtube channel

# How does it fit together

![Databricks%20Tutorial%20f4ab85ef14374675b8075ee73a51c22b/Untitled%201.png](Databricks%20Tutorial%20f4ab85ef14374675b8075ee73a51c22b/Untitled%201.png)

source from databricks youtube channel

# Exploring databricks workspace

- Workspace home screen -first thing when you login
- Navigation bar,shortcuts on workstream

Tasks [Link](https://docs.databricks.com/onboarding/paths/engineer/fundamentals.html)

- Create a cluster
- Create a notebook
- Create a table
- Query the table
- Display data
- Schedule a job

# Databricks architecture overview

December 08, 2020

The Databricks Unified Data Analytics Platform, from the original creators of Apache Spark, enables data teams to collaborate in order to solve some of the world’s toughest problems.

Databricks excels at enabling data scientists, data engineers, and data analysts to work together on uses cases like:

- Applying advanced analytics for machine learning and graph processing at scale
- Using deep learning for harnessing the power of unstructured data such for AI, image interpretation, automatic translation, natural language processing, and more
- Making data warehousing fast, simple, and scalable
- Proactively detecting threats with data science and AI
- Analyzing high-velocity sensor and time-series IoT data in real-time
- Making GDPR data subject requests easy to execute

# **High-level architecture**

Databricks is structured to enable secure cross-functional team collaboration while keeping a significant amount of backend services managed by Databricks so you can stay focused on your data science, data analytics, and data engineering tasks.

Although architectures can vary depending on custom configurations, the following diagram represents the most common structure and flow of data for Databricks on AWS environments.

![https://docs.databricks.com/_images/databricks-architecture.png](https://docs.databricks.com/_images/databricks-architecture.png)

Databricks operates out of a *control plane* and a *data plane*.

The *control plane* includes the backend services that Databricks manages in its own AWS account. Any commands that you run will exist in the control plane with your code fully encrypted. Saved commands reside in the data plane.

The *data plane* is managed by your AWS account and is where your data resides. This is also where data is processed. This diagram assumes that data has already been ingested into Databricks, but you can ingest data from external data sources, such as events data, streaming data, IoT data, and more. You can connect to external data sources outside of your AWS account for storage as well, using Databricks connectors.

Your data always resides in your AWS account in the data plane, not the control plane, so you always maintain full control and ownership of your data without lock-in.

# Development environments

Databricks has built-in notebooks for rapid iteration.  If you prefer an IDE or tool other than Databricks notebooks, the Databricks Connect library allows you to run code from a local machine on a remote Databricks cluster.
Databricks Connect allows you to connect your favorite IDE (IntelliJ, Eclipse, PyCharm, RStudio, Visual Studio), notebook server (Zeppelin, Jupyter), and other custom applications to Databricks clusters. [https://docs.databricks.com/dev-tools/databricks-connect.html](https://docs.databricks.com/dev-tools/databricks-connect.html)

# Set up your data architecture

One of the key constraints on making useful data-driven decisions is the structure, accessibility, and quality of the underlying data stores.

**Delta Lake**

Delta Lake. The Delta table format is a widely-used standard for enterprise data lakes at massive scale. Built on the foundation of another open source format—Parquet—Delta Lake adds advanced features and capabilities that enable additional robustness, speed, versioning, and data-warehouse-like ACID compliance. This is on top of the existing cost benefits of using existing cheap blob storage services.

[More about Delta Lake](https://databricks.com/discover/getting-started-with-delta-lake-tech-talks/making-apache-spark-better-with-delta-lake?_ga=2.210574165.1310724530.1615967991-1889218396.1600388830) and [here](https://databricks.com/discover/getting-started-with-delta-lake-tech-talks/simplify-scale-data-engineering-pipelines?_ga=2.151928441.1310724530.1615967991-1889218396.1600388830)

# Perform job scheduling and orchestration