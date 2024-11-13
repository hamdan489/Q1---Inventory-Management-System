
import sys

#  user data for authentication
users = {
    "admin": {"password": "admin", "role": "Admin"},
    "user": {"password": "user", "role": "User"}
}

# Products class 
products = {}

class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"{self.name} - {self.category} - ${self.price} - Stock: {self.stock_quantity}"

# Authentication 
def authenticate(username, password):
    user = users.get(username)
    if user and user["password"] == password:
        print(f"Welcome, {username}!")
        return user["role"]
    else:
        print("Invalid credentials.")
        return None

# Admin methods
def add_product():
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    stock_quantity = int(input("Enter stock quantity: "))
    products[product_id] = Product(product_id, name, category, price, stock_quantity)
    print(f"Product '{name}' added successfully.")

def edit_product():
    product_id = input("Enter product ID to edit: ")
    if product_id in products:
        product = products[product_id]
        product.name = input("Enter new name: ")
        product.category = input("Enter new category: ")
        product.price = float(input("Enter new price: "))
        product.stock_quantity = int(input("Enter new stock quantity: "))
        print("Product updated successfully.")
    else:
        print("Product not found.")

def delete_product():
    product_id = input("Enter product ID to delete: ")
    if product_id in products:
        del products[product_id]
        print("Product deleted successfully.")
    else:
        print("Product not found.")

# User functions
def view_inventory():
    if products:
        for product_id, product in products.items():
            print(f"{product_id}: {product}")
    else:
        print("Inventory is empty.")

def inventory_operations(role):
    while True:
        if role == "Admin":
            print("\n1. Add Product\n2. Edit Product\n3. Delete Product\n4. View Inventory\n5. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                add_product()
            elif choice == '2':
                edit_product()
            elif choice == '3':
                delete_product()
            elif choice == '4':
                view_inventory()
            elif choice == '5':
                sys.exit("Exiting program.")
            else:
                print("Invalid choice.")
        elif role == "User":
            print("\n1. View Inventory\n2. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                view_inventory()
            elif choice == '2':
                sys.exit("Exiting program.")
            else:
                print("Invalid choice.")

def main():
    print("Welcome to Inventory Management System")
    username = input("Username: ")
    password = input("Password: ")

    role = authenticate(username, password)
    if role:
        inventory_operations(role)

if __name__ == "__main__":
    main()
