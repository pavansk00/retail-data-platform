from pyspark.sql import SparkSession


def get_spark_session():

    spark = (
        SparkSession.builder
        .appName("RetailDataPlatform")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "8")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark