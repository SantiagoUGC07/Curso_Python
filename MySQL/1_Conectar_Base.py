import pymysql

connection = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='5538897909',
    db='seminario'
)
print(connection)
cursor = connection.cursor()
sql = "INSERT INTO persona(Nombre, ApellidoPaterno, ApellidoMaterno) values('Santiago','garcia','cordova')"
cursor.execute(sql)
connection.commit()

'''
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(version)'''


