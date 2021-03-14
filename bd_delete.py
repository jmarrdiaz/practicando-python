import pymysql

connection = pymysql.connect(
    host = "localhost",
    database = "test",
    user = "root",
    password = ""
    )

cursor = connection.cursor()

sql = "DELETE from users WHERE correo='usuario@example.com'"

cursor.execute(sql)

connection.commit()