import pymysql

connection = pymysql.connect(
    host = "localhost",
    database = "test",
    user = "root",
    password = ""
    )

cursor = connection.cursor()

sql = "SELECT * FROM users"

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()