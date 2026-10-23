import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.utils.spark_session import get_spark_session
from src.utils.config import load_config
from src.utils.logger import get_logger

def load_to_bronze():

    spark = get_spark_session()

    config = load_config()

    logger = get_logger()

    try:
        raw_path = config["paths"]["raw"]
        bronze_path = config["paths"]["bronze"]

        logger.info(f"Loading source files from raw to bronze")
        tables = [
            "customers",
            "products",
            "orders",
            "order_items"
        ]

        for table in tables:
            logger.info(f"reading the table {table}")

            df = spark.read.csv(
                f"{raw_path}/{table}.csv",
                inferSchema=True,
                header=True
            )

            print(f"\n {table.upper()}")
            print(f"Records: {df.count()}")
            df.printSchema()

            df.write.mode("overwrite").parquet(f"{bronze_path}/{table}")

            logger.info(f"table {table} loaded to bronze successfully")
    except Exception as e:
        logger.error(f"Failed to load data to bronze: {e}")
        raise
    finally:
        spark.stop()
        logger.info("Spark session stopped")

if __name__ == "__main__":
    load_to_bronze()    
