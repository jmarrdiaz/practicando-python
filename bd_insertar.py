import pymysql

connection = pymysql.connect(
    host = "localhost",
    database = "test",
    user = "root",
    password = ""
    )

cursor = connection.cursor()

sql = "INSERT INTO users(nombre, apellidos, correo) VALUES ('luis', 'cabrera', 'lcabrera@example.com')"

cursor.execute(sql)

connection.commit()