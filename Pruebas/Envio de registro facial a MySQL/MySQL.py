import pymysql
def envioDatos(Nombre,Fecha):
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='5538897909',
        db='seminario'
    )
    print(connection)
    cursor = connection.cursor()
    sql = "INSERT INTO persona(Nombre,ApellidoPaterno,ApellidoMaterno, Fecha) values('{}','null','null','{}')".format(Nombre,Fecha)
    cursor.execute(sql)
    connection.commit()
#envioDatos("santiago","12324")