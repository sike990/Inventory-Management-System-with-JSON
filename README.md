# Inventory Management System

A simple yet effective Python-based Inventory Management System designed for small businesses to track product sales, manage stock levels, and update inventory.

## Features

- Product sales processing
- Real-time inventory tracking
- Secure inventory updates with password protection
- Sales record generation
- JSON-based data storage

## Files

- `Main.py`: Handles product sales and updates inventory
- `Updating_inventory.py`: Allows authorized users to modify stock levels
- `Records.json`: Stores product information and quantities
- `Sales.txt`: Logs all sales transactions

## Usage

1. Run `Main.py` to process sales:
   - View available products
   - Enter customer details
   - Select product and quantity
   - Generate bill and update inventory

2. Run `Updating_inventory.py` to modify stock levels:
   - Enter password for authorization
   - Update quantities for specific products

## Requirements

- Python 3.x
- JSON library (included in Python standard library)

## Setup

1. Clone the repository
2. Ensure `Records.json` is in the same directory as the Python scripts
3. Run the desired script (`Main.py` or `Updating_inventory.py`)

## Future Improvements

- Graphical user interface
- Database integration for larger inventories
- Advanced reporting and analytics features

## Contributing

Contributions, issues, and feature requests are welcome.
