import psycopg2, csv

# connection to the database
conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "Diora040917"
)

current = conn.cursor()

sql = " INSERT INTO PhoneBook VALUES(%s, %s, %s, %s) returning *; "

try:
    result = []
    with open('pp2-21B050634\phonebook.csv', 'r') as f:
        reader = csv.reader(f, delimiter = ', ')
        for row in reader:
            current.execute(sql, row)
            result.append(current.fetchone())
        print(result)


current.close()
conn.commit()
conn.close()       
