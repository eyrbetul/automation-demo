import csv
import os

base_dir = os.path.dirname(__file__)
input_file = os.path.join(base_dir, "orders.csv")
output_file = os.path.join(base_dir, "processed_orders.csv")

with open(input_file, mode="r") as file:
    reader = csv.DictReader(file)
    orders = list(reader)

processed = []

for order in orders:
    unit_price = int(order["unit_price"])
    quantity = int(order["quantity"])
    total = unit_price * quantity

    if quantity > 5:
        bulk_order = "Yes"
    else:
        bulk_order = "No"

    if total >= 1000:
        priority = "High"
    else:
        priority = "Normal"

    processed.append({
        "order_id": order["order_id"],
        "customer_name": order["customer_name"],
        "category": order["product_category"],
        "total_price": total,
        "priority": priority,
        "bulk_order": bulk_order })

with open(output_file, mode="w", newline="") as file:
    fieldnames = ["order_id", "customer_name", "category", "total_price", "priority", "bulk_order"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(processed)


print("Orders processed successfully.")