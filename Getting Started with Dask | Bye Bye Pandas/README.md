# Dask Tutorial

Bye-bye Pandas, hello dask!

- [x]  Introduction
- [x]  What is dask?
- [x]  Why Dask? (Current Challenges with Data science libraries)
- [x]  Installing dask for local development
- [x]  Reading through dask
- [x]  Few manipulation through dask
- [x]  Architecture of Dask
- [x]  Dask Vs Pandas [https://docs.dask.org/en/latest/dataframe.html](https://docs.dask.org/en/latest/dataframe.html)
- [x]  Dask Vs Spark
- [x]  Outro

Dask Vs Pandas
A Dask dataframe consists of multiple smaller pandas dataframes. A large pandas dataframe splits row-wise to form multiple smaller dataframes. These smaller dataframes are present on a disk of a single machine, or multiple machines (thus allowing to store datasets of size larger than the memory). Each computation on a Dask dataframe parallelizes operations on the existing pandas dataframes.

Dask Vs Spark

One very common question that I have seen while exploring Dask is: How is Dask different from Spark and which one is preferred? There is no hard and fast rule that says one should use Dask (or Spark), but you can make your choice based on the features offered by them and whichever one suits your requirements more.

Here are some important differences between Dask and Spark :

[]()

![https://cdn.analyticsvidhya.com/wp-content/uploads/2018/08/Dask-Spark.png](https://cdn.analyticsvidhya.com/wp-content/uploads/2018/08/Dask-Spark.png)

![https://cdn.analyticsvidhya.com/wp-content/uploads/2018/08/Dask-Spark.png](https://cdn.analyticsvidhya.com/wp-content/uploads/2018/08/Dask-Spark.png)

# References

[https://docs.dask.org/en/latest/](https://docs.dask.org/en/latest/)

[https://docs.dask.org/en/latest/why.html](https://docs.dask.org/en/latest/why.html)

[https://www.analyticsvidhya.com/blog/2018/08/dask-big-datasets-machine_learning-python/](https://www.analyticsvidhya.com/blog/2018/08/dask-big-datasets-machine_learning-python/)