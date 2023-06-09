import sqlite3

# connect to database

conn = sqlite3.connect('Supershop.db')

conn.execute('''CREATE TABLE IF NOT EXISTS product
             (productID INT PRIMARY KEY,
             productName TEXT,
             quantity INT,
             price FLOAT)''')

conn.execute("DELETE FROM product")

# product data

product_data = [(10, "Jean", 50, 89.99),
                (20, "Shirt", 67, 59.99),
                (30, "Tshirt", 88, 39.99)]

conn.executemany('INSERT INTO product (productID, productName, quantity, price) VALUES (?, ?, ?, ?)', product_data)

cursor = conn.execute("SELECT * FROM product")

print("Welcome to the SuperShop Program!")

options = [
    "\nIf you want to buy a product, enter 1.",
    "If you want to log in as admin, enter 2.",
    "If you want to quit, enter 0."
]

# user selection

while True:
    print("\n".join(options))

    selection = input("Enter your selection: ")

# Display a list of products and prices to the screen with instructions for customers to order products

    if selection == "1":
        print("productID  " + "productName  " + "quantity  " + "price")

        # Retrieve the updated product list from the database
        cursor.execute("SELECT * FROM product")
        updated_product_data = cursor.fetchall()

        for row in updated_product_data:
            print(str(row[0]) + ",\t   " + str(row[1]) + ",\t " + str(row[2]) + ",\t  " + str(row[3]))

        order = {}  # Dictionary to store the selected products and quantities

        while True:
            product_id = input("\nEnter the product ID of your choice (or 'done' to finish): ")

            if product_id == "done":
                break

            # Check if the entered product ID exists in the database
            cursor.execute("SELECT * FROM product WHERE productID = ?", (product_id,))
            product = cursor.fetchone()

            # Calculate total price, display total price, and ask customer to confirm order

            if product:
                quantity = input("Enter the quantity for product ID {}: ".format(product_id))
                if int(quantity) > product[2]:
                    print("Cannot order more than the available stock.")
                else:
                    order[product] = int(quantity)
            else:
                print("Invalid product ID entered. Try again.")

        total_price = 0.0

        print("\nOrdered Products:")
        for product, quantity in order.items():
            product_name = product[1]
            product_price = product[3]
            subtotal = product_price * quantity
            total_price += subtotal
            print("Product: {}, Quantity: {}, Subtotal: ${:.2f}".format(product_name, quantity, subtotal))
            # Update the database with the new quantity after the order
            new_quantity = product[2] - quantity
            conn.execute("UPDATE product SET quantity = ? WHERE productID = ?", (new_quantity, product[0]))
            conn.commit()

        print("Total Price: ${:.2f}".format(total_price))

        # Update the product_data list with the new quantity after the order
        for product in order:
            for i, p in enumerate(updated_product_data):
                if p[0] == product[0]:
                    updated_product_data[i] = (p[0], p[1], p[2] - order[product], p[3])
                    break

        confirm = input("Do you want to confirm the order? (yes/no): ")

        if confirm.lower() == "yes":
            print("Order confirmed. Thank you!")
        else:
            print("Order cancelled.")

#Loop Jean

    elif selection == "0":
        break
    else:
        print("Invalid number entered. Try again.")
