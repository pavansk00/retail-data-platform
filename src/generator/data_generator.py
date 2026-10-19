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

from datetime import datetime

def generate_orders(
    customer_count=1000,
    n=3000
):

    statuses = [
        "COMPLETED",
        "PENDING",
        "CANCELLED",
        "RETURNED"
    ]

    orders = []

    for order_id in range(1, n + 1):

        orders.append(
            {
                "order_id": order_id,
                "customer_id": random.randint(
                    1,
                    customer_count
                ),
                "order_date": fake.date_between(
                    start_date="-2y",
                    end_date="today"
                ),
                "order_status": random.choice(
                    statuses
                )
            }
        )

    pd.DataFrame(orders).to_csv(
        f"{RAW_PATH}/orders.csv",
        index=False
    )

    print(f"Generated {n} orders")

def generate_order_items(
    order_count=3000,
    product_count=100,
    n=10000
):

    order_items = []

    for item_id in range(1, n + 1):

        quantity = random.randint(1, 5)

        unit_price = round(
            random.uniform(100, 10000),
            2
        )

        order_items.append(
            {
                "order_item_id": item_id,
                "order_id": random.randint(
                    1,
                    order_count
                ),
                "product_id": random.randint(
                    1,
                    product_count
                ),
                "quantity": quantity,
                "unit_price": unit_price
            }
        )

    pd.DataFrame(order_items).to_csv(
        f"{RAW_PATH}/order_items.csv",
        index=False
    )

    print(
        f"Generated {n} order items"
    )

if __name__ == "__main__":

    generate_customers(1000)
    generate_products(100)
    generate_orders(
        customer_count=1000,
        n=3000
    )

    generate_order_items(
        order_count=3000,
        product_count=100,
        n=10000
    )