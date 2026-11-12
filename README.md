# 🛒 Smart Grocery Store Management System

A professional **console-based Python application** for managing products, inventory, customer sales, and store reports.

This project is designed as a practical Python programming assignment and demonstrates the use of **lists, dictionaries, functions, loops, conditional statements, input validation, and basic data processing**.

## 📌 Project Overview

The Smart Grocery Store Management System helps a local grocery store manage its daily operations through a simple menu-driven interface.

The application allows the store owner to:

- Add new products
- View all available products
- Search products by ID or name
- Update product stock
- Process customer sales
- Maintain sales records
- Generate a complete store report

## ✨ Features

### 1. Product Management
Products are stored in a **list of dictionaries**.

Each product contains:

- Product ID
- Product Name
- Category
- Price
- Available Stock

### 2. Add New Product
- Accepts product information from the user
- Stores each product as a dictionary
- Uses `.append()` to add the product to the products list
- Prevents duplicate product IDs
- Validates user input

### 3. View All Products
Displays product information in a readable format, including:

- ID
- Name
- Category
- Price
- Stock

### 4. Search Product
Products can be searched using:

- Product ID
- Product Name

The search is case-insensitive for product names.

### 5. Update Product Stock
The application provides two stock-management options:

- Add stock to the existing quantity
- Set a completely new stock quantity

### 6. Process Customer Sale
The system:

1. Finds the requested product
2. Checks available stock
3. Validates the purchase quantity
4. Calculates the total price
5. Deducts sold quantity from stock
6. Stores the completed sale
7. Displays a purchase summary

Sales are rejected when the requested quantity is greater than available stock.

### 7. Sales Records
Completed transactions are stored separately as dictionaries containing:

- Product ID
- Product Name
- Quantity Sold
- Total Amount

### 8. Store Report
The report displays:

- Total number of products
- Total available stock
- Total sales transactions
- Total revenue
- Products with stock below 5 units
- Product with the highest price
- Product with the lowest price

## 🧰 Technologies Used

- **Python 3**
- Python Standard Library only
- Lists
- Dictionaries
- Functions
- `for` and `while` loops
- `if / elif / else`
- Input validation
- Basic arithmetic operations

No external packages are required.

## 📂 Project Structure

```text
smart-grocery-store/
│
├── grocery_store.py
├── README.md
└── .gitignore
```

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Open the Project Folder

Open a terminal inside the project folder.

### Step 3: Run the Program

```bash
python grocery_store.py
```

On some systems:

```bash
python3 grocery_store.py
```

## 🖥️ Application Menu

```text
========================================
SMART GROCERY STORE SYSTEM
========================================

1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice:
```

## 🧪 Example Workflow

### Add a Product

```text
Enter Product ID: 104
Enter Product Name: Eggs
Enter Category: Dairy
Enter Price: Rs. 300
Enter Available Stock: 15

Product 'Eggs' added successfully.
```

### Process a Sale

```text
Enter Product ID: 101
Enter Purchase Quantity: 2

Product: Milk
Price: Rs. 250.00
Available Stock: 20

--- Purchase Summary ---
Product       : Milk
Quantity       : 2
Price per unit : Rs. 250.00
Total Amount   : Rs. 500.00
Remaining Stock: 18 units

Sale completed successfully.
```

## 📚 Python Concepts Demonstrated

| Concept | Usage |
|---|---|
| List | Store products and sales |
| Dictionary | Store product and sale details |
| `.append()` | Add products and sales |
| Functions | Separate application operations |
| `for` loop | Process products and sales |
| `while` loop | Keep the menu running |
| Conditional statements | Handle menu choices and validation |
| Dictionary keys | Access product/sale information |
| Input validation | Handle invalid user input |
| Arithmetic | Calculate sales and revenue |

## 🔐 Input Validation

The application validates important user inputs, including:

- Product IDs must be positive integers
- Product names cannot be empty
- Categories cannot be empty
- Prices must be greater than zero
- Stock quantities cannot be negative
- Sale quantities must be positive
- Duplicate product IDs are not allowed
- Sales cannot exceed available stock
- Invalid menu choices are handled safely

## 💡 Learning Objective

This project provides practical experience in building a small real-world Python application using fundamental programming concepts.

It is especially useful for practicing:

- Data organization
- Functions
- Loops
- Conditions
- Lists and dictionaries
- User input
- Validation
- Inventory calculations
- Transaction processing

## 🚀 Future Improvements

Possible future enhancements include:

- Save products and sales to a JSON or CSV file
- Add product deletion
- Add product editing
- Add customer information
- Add daily/monthly sales reports
- Add login/authentication
- Connect the application to a database
- Build a graphical or web interface

## 👤 Author

Developed as a Python programming project demonstrating fundamental programming and data-management concepts.

## 📄 License

This project is intended for educational and learning purposes.
