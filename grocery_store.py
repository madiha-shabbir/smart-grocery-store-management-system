"""
Smart Grocery Store Management System
------------------------------------
A console-based Python application for managing grocery products,
inventory, customer sales, and store reports.

This project uses:
- Lists of dictionaries
- Functions
- Loops
- Conditional statements
- Input validation
- Dictionary keys and values
"""

products = [
    {
        "id": 101,
        "name": "Milk",
        "category": "Dairy",
        "price": 250.0,
        "stock": 20
    },
    {
        "id": 102,
        "name": "Bread",
        "category": "Bakery",
        "price": 150.0,
        "stock": 10
    },
    {
        "id": 103,
        "name": "Rice",
        "category": "Grains",
        "price": 500.0,
        "stock": 8
    }
]

sales = []


def display_product(product):
    """Display complete information for one product."""
    print(f"ID       : {product['id']}")
    print(f"Name     : {product['name']}")
    print(f"Category : {product['category']}")
    print(f"Price    : Rs. {product['price']:.2f}")
    print(f"Stock    : {product['stock']} units")
    print("-" * 40)


def find_product_by_id(product_id):
    """Return a product by ID, or None if it does not exist."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def get_positive_int(prompt):
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_negative_int(prompt):
    """Get a non-negative integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter 0 or a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_positive_float(prompt):
    """Get a positive price value from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Price must be greater than 0.")
        except ValueError:
            print("Invalid price. Please enter a valid number.")


def add_product():
    """Add a new product while preventing duplicate IDs."""
    print("\n--- Add New Product ---")

    product_id = get_positive_int("Enter Product ID: ")

    if find_product_by_id(product_id) is not None:
        print("A product with this ID already exists.")
        return

    name = input("Enter Product Name: ").strip()
    while not name:
        print("Product name cannot be empty.")
        name = input("Enter Product Name: ").strip()

    category = input("Enter Category: ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Enter Category: ").strip()

    price = get_positive_float("Enter Price: Rs. ")
    stock = get_non_negative_int("Enter Available Stock: ")

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    products.append(product)
    print(f"Product '{name}' added successfully.")


def view_all_products():
    """Display all products."""
    print("\n--- All Products ---")

    if not products:
        print("No products are available.")
        return

    for product in products:
        display_product(product)


def search_product():
    """Search for a product by ID or name."""
    print("\n--- Search Product ---")
    search_value = input("Enter Product ID or Product Name: ").strip()

    if not search_value:
        print("Search value cannot be empty.")
        return

    # Search by numeric ID when possible.
    if search_value.isdigit():
        product = find_product_by_id(int(search_value))
        if product:
            print("\nProduct found:")
            display_product(product)
            return

    # Search by name without case sensitivity.
    for product in products:
        if product["name"].lower() == search_value.lower():
            print("\nProduct found:")
            display_product(product)
            return

    print("Product not found.")


def update_product_stock():
    """Add stock or replace the current stock quantity."""
    print("\n--- Update Product Stock ---")

    product_id = get_positive_int("Enter Product ID: ")
    product = find_product_by_id(product_id)

    if product is None:
        print("Product not found.")
        return

    print(f"Current stock for {product['name']}: {product['stock']} units")
    print("1. Add Stock")
    print("2. Set New Stock Quantity")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            quantity = get_positive_int("Enter quantity to add: ")
            product["stock"] += quantity
            print(f"Stock updated. New stock: {product['stock']} units")
            return

        if choice == "2":
            new_stock = get_non_negative_int("Enter new stock quantity: ")
            product["stock"] = new_stock
            print(f"Stock updated. New stock: {product['stock']} units")
            return

        print("Invalid choice. Please select 1 or 2.")


def process_customer_sale():
    """Process a sale, update stock, and save the sales record."""
    print("\n--- Process Customer Sale ---")

    product_id = get_positive_int("Enter Product ID: ")
    product = find_product_by_id(product_id)

    if product is None:
        print("Product not found.")
        return

    print(f"Product: {product['name']}")
    print(f"Price: Rs. {product['price']:.2f}")
    print(f"Available Stock: {product['stock']} units")

    quantity = get_positive_int("Enter Purchase Quantity: ")

    if quantity > product["stock"]:
        print(
            f"Insufficient stock. Only {product['stock']} "
            "units are available."
        )
        return

    total_amount = product["price"] * quantity

    # Deduct sold quantity from available stock.
    product["stock"] -= quantity

    sale = {
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity": quantity,
        "total_amount": total_amount
    }

    # Store the completed sale in the sales list.
    sales.append(sale)

    print("\n--- Purchase Summary ---")
    print(f"Product       : {product['name']}")
    print(f"Quantity       : {quantity}")
    print(f"Price per unit : Rs. {product['price']:.2f}")
    print(f"Total Amount   : Rs. {total_amount:.2f}")
    print(f"Remaining Stock: {product['stock']} units")
    print("Sale completed successfully.")


def view_sales_records():
    """Display all completed sales."""
    print("\n--- Sales Records ---")

    if not sales:
        print("No sales records available.")
        return

    for index, sale in enumerate(sales, start=1):
        print(f"Sale #{index}")
        print(f"Product ID   : {sale['product_id']}")
        print(f"Product Name : {sale['product_name']}")
        print(f"Quantity Sold: {sale['quantity']}")
        print(f"Total Amount : Rs. {sale['total_amount']:.2f}")
        print("-" * 40)


def generate_store_report():
    """Generate a summary report for inventory and sales."""
    print("\n--- Store Report ---")

    total_products = len(products)

    total_stock = 0
    for product in products:
        total_stock += product["stock"]

    total_transactions = len(sales)

    total_revenue = 0
    for sale in sales:
        total_revenue += sale["total_amount"]

    low_stock_products = []
    for product in products:
        if product["stock"] < 5:
            low_stock_products.append(product)

    print(f"Total Products       : {total_products}")
    print(f"Total Available Stock: {total_stock} units")
    print(f"Total Sales           : {total_transactions}")
    print(f"Total Revenue         : Rs. {total_revenue:.2f}")

    print("\nProducts with Stock Below 5 Units:")
    if low_stock_products:
        for product in low_stock_products:
            print(f"- {product['name']}: {product['stock']} units")
    else:
        print("No products are currently below 5 units.")

    if products:
        highest_price_product = max(products, key=lambda item: item["price"])
        lowest_price_product = min(products, key=lambda item: item["price"])

        print("\nHighest Price Product:")
        print(
            f"- {highest_price_product['name']} "
            f"(Rs. {highest_price_product['price']:.2f})"
        )

        print("\nLowest Price Product:")
        print(
            f"- {lowest_price_product['name']} "
            f"(Rs. {lowest_price_product['price']:.2f})"
        )
    else:
        print("\nNo products available for price comparison.")


def display_menu():
    """Display the main application menu."""
    print("\n" + "=" * 40)
    print("SMART GROCERY STORE SYSTEM")
    print("=" * 40)
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")


def main():
    """Run the main menu loop."""
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product_stock()
        elif choice == "5":
            process_customer_sale()
        elif choice == "6":
            view_sales_records()
        elif choice == "7":
            generate_store_report()
        elif choice == "8":
            print("\nThank you for using Smart Grocery Store System.")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 8.")


if __name__ == "__main__":
    main()
