import  psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Diora040917"
)

current = conn.cursor()

sql = """
    CREATE TABLE snake(
        user_name VARCHAR(20),
        highscore INT DEFAULT(0),
        user_score INT DEFAULT(0),
        level INT DEFAULT(0)
    );
"""

current.execute(sql)

current.close()
conn.commit()
conn.close()
