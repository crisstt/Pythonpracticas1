import mysql.connector
class Username:

    cnn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'rosado1988',
                                  database= 'formuser')

    def str():
        pass

    def consulta_username():
        cur = cnn.cursor()
        cur.execute("SELECT * FROM users")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_username(Id):
        cur = cnn.cursor()
        sql = "SELECT * FROM users WHERE Id = {}". FORMAT(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def inserta_username(Username,Password,Fullname,Age):
        cur = cnn.cursor()
        sql= '''INSERT INTO users (Username,Password,Fullname,Age)
        VALUES (' {} ',' {} ',' {} ',' {} ')'''. format (Username,Password,Fullname,Age)
        cur.execute(sql)
        n=cur.rowcount
        cnn.commit()
        cur.close()
        return n

    def elimina_username(Id):
        cur = cnn.cursor()
        sql = '''DELETE FROM users WHERE Id = {} '''. format(Id)
        cur.execute(sql)
        n = cur.rowcount
        cnn.commit()
        cur.close()
        return n

    def modifica_username(Id, Username,Password,Fullname,Age):
        cur = cnn.cursor()
        sql= '''UPDATE users SET Username = ' {} ', Password = ' {} ', Fullname = ' {} ', Age = {}  '''. format(Username,Password,Fullname,Age)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n


    

