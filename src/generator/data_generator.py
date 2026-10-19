from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("en_IN")

RAW_PATH = "data/raw"

Path(RAW_PATH).mkdir(parents=True, exist_ok=True)


def generate_customers(n=1000):

    customers = []

    for customer_id in range(1, n + 1):

        customers.append(
            {
                "customer_id": customer_id,
                "customer_name": fake.name(),
                "email": fake.email(),
                "city": fake.city(),
                "state": fake.state(),
                "registration_date": fake.date_between(
                    start_date="-3y",
                    end_date="today"
                )
            }
        )

    pd.DataFrame(customers).to_csv(
        f"{RAW_PATH}/customers.csv",
        index=False
    )

    print(f"Generated {n} customers")

def generate_products(n=100):

    categories = [
        "Electronics",
        "Fashion",
        "Home",
        "Sports",
        "Books",
        "Beauty",
        "Toys"
    ]

    products = []

    for product_id in range(1, n + 1):

        products.append(
            {
                "product_id": product_id,
                "product_name": f"Product_{product_id}",
                "category": random.choice(categories),
                "price": round(
                    random.uniform(100, 10000),
                    2
                )
            }
        )

    pd.DataFrame(products).to_csv(
        f"{RAW_PATH}/products.csv",
        index=False
    )

    print(f"Generated {n} products")

if __name__ == "__main__":

    generate_customers(1000)
    generate_products(100)