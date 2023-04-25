import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "Diora040917"
)

current = conn.cursor()

sql = " UPDATE PhoneBook SET phone_number = %s WHERE account_name = %s; "
account_name = input()
phone_number = input()

current = execute(sql, (phone_number, account_name))

current.close()
conn.commit()
conn.close()
