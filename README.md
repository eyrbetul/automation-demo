# Order Processing Automation

This project is a simple Python-based automation tool that processes business order data from a CSV file and generates an enriched output file with calculated fields.

It was built as a beginner-friendly project to practice Python fundamentals and understand how data processing workflows can be automated.

---

## How to Run

Make sure you have Python installed, then run the script from the project directory:

```bash
python3 main.py
```
## Features

- Reads order data from a CSV file (orders.csv)
- Parses and processes each order
- Calculates total price (unit_price × quantity)
  
- Classifies orders as:
  - Bulk orders (quantity > threshold)
  - Normal orders
  
- Assigns priority levels:
  - High (if total price exceeds threshold)
  - Normal otherwise
  
- Generates a new enriched CSV file (processed_orders.csv)

## Output Example

The script generates a new file:
processed_orders.csv

This file includes additional computed fields such as:
- total_price
- priority (High / Normal)
- bulk_order (Yes / No)

## Purpose

The goal of this project is to practice:
- File handling in Python
- Working with CSV data
- Basic data transformation
- Automation logic using conditions
- Structuring a simple Python project
  
It demonstrates how manual spreadsheet-like tasks can be automated using Python.


