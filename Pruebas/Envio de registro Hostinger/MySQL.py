import pymysql
def envioDatos(Nombre,Fecha):
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='u614989997_admindb',
        password='6TUH72toIDh5RpVGBi',
        db='u614989997_db_inventario'
    )
    print(connection)
    '''
    cursor = connection.cursor()
    sql = "INSERT INTO persona(Nombre,ApellidoPaterno,ApellidoMaterno, Fecha) values('{}','null','null','{}')".format(Nombre,Fecha)
    cursor.execute(sql)
    connection.commit()
    '''
envioDatos("santiago","12324")