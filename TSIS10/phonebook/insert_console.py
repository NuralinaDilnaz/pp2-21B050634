import psycopg2

# connection to the database
conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "Diora040917"
)

current = conn.cursor()

sql = " INSERT INTO PhoneBook VALUES(%s, %s, %s, %s) returning *; "

except Exception as e:
    id = input("Enter the number:")
    account_name = input("Enter the name:")
    phone_number = input("Enter the phone number:")
    address = input("Enter the address:")  

current.close()
conn.commit()
conn.close()       
