from src.utils.spark_session import get_spark_session
from src.utils.config import load_config
from src.utils.logger import get_logger

def main():
    spark = get_spark_session()

    try:
        config = load_config()
        logger = get_logger()

        logger.info("Pipeline Started")

        print("Spark Version:", spark.version)
        print(config)

        logger.info("Pipeline Initialized")

    finally:
        spark.stop()

if __name__ == "__main__":
    main()
