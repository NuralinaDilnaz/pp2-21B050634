import psycopg2

# connection to the database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Diora040917"
)

current = conn.cursor()

sql="""
    CREATE TABLE PhoneBook(
        id VARCHAR PRIMARY KEY,
        account_name VARCHAR,
        phone_number VARCHAR,
        address VARCHAR
    );
"""
# create table
current.execute(sql)
# close communication with the PostgreSQL database server
current.close()
# commit the changes
conn.commit()
# close the changes
conn.close() 