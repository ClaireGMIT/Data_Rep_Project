import mysql.connector
import dbconfig as cfg

class tabletsDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )
      
    def create(self, tabprdn):
        cursor = self.db.cursor()
        sql = "insert into tabprdn (Batch_No, API_Lot_No, API_Particle_Size, Screen_Size, Blend_Time, Compressor, Inlet_Temp, Spray_Rate, Dissolution) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = [
            tabprdn['Batch_No'],
            tabprdn['API_Lot_No'],
            tabprdn['API_Particle_Size'],
            tabprdn['Screen_Size'],
            tabprdn['Blend_Time'],
            tabprdn['Compressor'],
            tabprdn['Inlet_Temp'],
            tabprdn['Spray_Rate'],
            tabprdn['Dissolution']
       ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from tabprdn"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = [] #to create dict items
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def findByID(self, Batch_No):   
        cursor = self.db.cursor()
        sql="select * from tabprdn where Batch_No = %s"
        values = [Batch_No]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
    
    def update(self, tabprdn):
        cursor = self.db.cursor()
        sql= "UPDATE tabprdn SET API_Lot_No=%s, API_Particle_Size=%s, Screen_Size=%s, Blend_Time=%s, Compressor=%s, Inlet_Temp=%s, Spray_Rate=%s, Dissolution=%s WHERE Batch_No = %s"
        values = [
            tabprdn['API_Lot_No'],
            tabprdn['API_Particle_Size'],
            tabprdn['Screen_Size'],
            tabprdn['Blend_Time'],
            tabprdn['Compressor'],
            tabprdn['Inlet_Temp'],
            tabprdn['Spray_Rate'],
            tabprdn['Dissolution'],
            tabprdn['Batch_No']
       ]
        cursor.execute(sql, values)
        self.db.commit()
        return tabprdn

    def delete(self, Batch_No):
        cursor = self.db.cursor()
        sql="delete from tabprdn where Batch_No = %s"
        values = (Batch_No,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDict(self, result):
        colnames = ['Batch_No', 'API_Lot_No', 'API_Particle_Size', 'Screen_Size', 'Blend_Time', 'Compressor', 'Inlet_Temp', 'Spray_Rate', 'Dissolution']
        tabprdn = {}
        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                tabprdn[colName] = value
            return tabprdn

tabletsDAO = tabletsDAO()