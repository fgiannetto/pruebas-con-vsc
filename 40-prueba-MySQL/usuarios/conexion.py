import mysql.connector

def conectar():

    database = mysql.connector.connect(
        user = "Franco",
        password = "Franco",
        host = "10.10.2.29",
        #host = "127.0.0.1",
        #host = "10.10.2.100",        
        #host = "200.69.141.154",
        database = "master_python",
        port = 3306
    )

    #print (database)

    cursor = database.cursor(buffered=True)

    return [database, cursor]



"""
    database = mysql.connector.connect(
        user = 'root',
        password = 'root',
        #host = '10.10.2.29',
        host = '127.0.0.1',
        #host = '10.10.2.100',        
        #host = 'localhost',
        database = 'master_python',
        port = 3306
    )
"""