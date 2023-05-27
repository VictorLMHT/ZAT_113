# Assessment Task 3 - ZAT 113
# Jean Audoin and Victor Le Méhauté

#import sqlite3
import sqlite3
import hashlib

#connect to database called 'admin.db'
connection = sqlite3.connect('admin.db')

#Create cursor object for interacting with database
cursor = connection.cursor()

#Create a variable for the SQL statement which is written as a string
command1 = """CREATE TABLE IF NOT EXISTS login (
        username_hashed  text PRIMARY KEY,
        password_hashed text
);"""

cursor.execute(command1)

# ashes admin login info to protect them with hashlib.sha256 method
username = "VicoEtJean"
password = "SuperShop.10"
usernameHashDb = hashlib.sha256(username.encode()).hexdigest()
passwordHashDb = hashlib.sha256(password.encode()).hexdigest()


#Add 1 row to llogin table using SQL INSERT statements passed into .execute() method as strings
cursor.execute("INSERT OR IGNORE INTO login VALUES(?, ?);", (usernameHashDb, passwordHashDb))

#Save (commit) the changes
connection.commit()



#The admin login loop function
def validatePassword():
    while True:
        # Prompt user for info
        usernameInput = input("Enter username: ")
        passwordInput = input("Enter password: ")

        # Hash user login info
        usernameInputHashed = hashlib.sha256(usernameInput.encode()).hexdigest()
        passwordInputHashed = hashlib.sha256(passwordInput.encode()).hexdigest()

        # Retrieve the stored password from the database
        cursor.execute("SELECT password_hashed FROM login WHERE username_hashed = ?", (usernameInputHashed,))
        result = cursor.fetchone()

        if result:  # retrieves the stored password from the query result
            storedPassword = result[0]
    
            # Compare the stored hash with the input hash
            if storedPassword == passwordInputHashed:
                print("Password is correct!")
                break
            else:
                print("Password is incorrect!")
              
        else:
            print("Username not found!")
            
# Display Product and prices from the product DB
def displayProduct():  # Voir avec Vico         


# Allows to add new product in the DB
def addProduct():
    productId = input("Enter new product ID: ")
    poductName = input ("Enter new product name: ")
    productQuantity = input ("Enter new product quantity: ")
    productPrice = input ("Enter new product unit price: ")

    cursor.execute("INSERT INTO product VALUES (?,?,?,?);",(productId,poductName, productQuantity, productPrice)

##print("Welcome to the New Trend Shop \n") #Welcomming message
##
##print("""Main Menu 
##---------------""")
        

# login validation method
validatePassword()

# Display Product and prices from the product DB
displayProduct()

# Admin Menu list    
selectList = [
        "If you want to go back to the main menu, enter 1. \n"
        "If you want to add a new product in the database, enter 2. \n"
        "If you want to update an existing product in the database, enter 3. \n"
        " If you want to quit, enter 0. \n"
        ]


while True :
    # Displays user's options
    for option in selectList :
    print(option)

    # Go back to the main menu
    if selection == 1
    break #breaks the admin loop

    elif selection == 2
        addProduct()

    elif selection == 3
        updateProduct()
        
    elif selection == 0
        print(" \n Thanks for visiting New Trend Shop")


#Close the database connection
connection.close()
