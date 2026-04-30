import csv
import os

base_dir = os.path.dirname(__file__)
input_file = os.path.join(base_dir, "orders.csv")
output_file = os.path.join(base_dir, "processed_orders.csv")

BULK_THRESHOLD = 5
HIGH_PRIORITY_THRESHOLD = 1000

orders = []

with open(input_file, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        orders.append(row)

processed = []

for order in orders:
    try:
        unit_price = int(order.get("unit_price", 0))
        quantity = int(order.get("quantity", 0))

        total_price = unit_price * quantity

        bulk_order = "Yes" if quantity > BULK_THRESHOLD else "No"
        priority = "High" if total_price >= HIGH_PRIORITY_THRESHOLD else "Normal"

        processed.append({
            "order_id": order.get("order_id"),
            "customer_name": order.get("customer_name"),
            "category": order.get("product_category"),
            "total_price": total_price,
            "priority": priority,
            "bulk_order": bulk_order
        })

    except Exception as e:
        print(f"Error processing order {order}: {e}")

with open(output_file, mode="w", newline="") as file:
    fieldnames = ["order_id", "customer_name", "category", "total_price", "priority", "bulk_order"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(processed)


print("Orders processed successfully.")
print(f"Total orders processed: {len(processed)}")
print(f"Output file created: {output_file}")