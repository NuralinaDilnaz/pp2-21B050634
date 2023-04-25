import psycopg2

# connection to the database
conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "Diora040917"
)

current = conn.cursor()

sql = " SELECT * FROM PhoneBook; "

current = execute(sql)

result = current.fetchall()

print(result)

current.close()
conn.commit()
conn.close()