import pymysql

connection = pymysql.connect(
    host = "localhost",
    database = "test",
    user = "root",
    password = ""
    )

cursor = connection.cursor()

sql = "UPDATE users SET correo='apalacios@example.com' WHERE nombre='andrea'"

cursor.execute(sql)

connection.commit()