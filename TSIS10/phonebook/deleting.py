import psycopg2

#connection to the database
conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "Diora040917"
)

current=conn.cursor()

sql = " DELETE FROM PhoneBook WHERE account_name = %s; "
account_name = input()

current.execute(sql, (account_name))

current.close()
conn.commit()
conn.close() 
