import sqlite3


conn = sqlite3.connect('Supershop.db')

conn.execute('''CREATE TABLE IF NOT EXISTS product
             (productID INT PRIMARY KEY,
             productName TEXT,
             quantity INT,
             price FLOAT)''')


conn.execute("DELETE FROM product")

product_data = [(10, "Jean", 50, 89.99),
                  (20, "Shirt", 67, 59.99),
                  (30, "Tshirt", 88, 39.99)]

conn.executemany('INSERT INTO product (productID, productName, quantity, price) VALUES (?, ?, ?, ?)', product_data)

cursor = conn.execute("SELECT * FROM product")

print("Welcome to the SuperShop Program!")

options = ["\n"
           "If you want to buy product, enter 1.",
           "If you want to log as admin, enter 2.",
           "If you want to quit, enter 0."]

while True:
    print("\n".join(options))

    selection = input("Enter your selection: ")

    if selection == "1":
        print("productID  " + "productName  " + "quantity  " + "price")

        for row in cursor:
            print(str(row[0]) + ",\t   " + str(row[1]) + ",\t " + str(row[2]) + ",\t  " + str(row[3]))


        print("\n Do you want to buy a product ?")
        selection = input("Enter the product ID of your choice: ")

        if selection == 10 or 20 or 30 :
            print ("caca")
#Boucle Jean


    elif selection == "0":
        break
    else:
        print("Invalid number entered. Try again.")
