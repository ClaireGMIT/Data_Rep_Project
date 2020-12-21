import mysql.connector

class ProductionDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Tablet_Dissolution"
        )

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into production (Batch_No, API_Particle_Size, Screen_Size, Blend_Time, Compressor, Inlet_Temp, Spray_Rate, Dissolution) values (%s,%s, %s,%s, %s,%s, %s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from production"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def findByID(self, Batch_No):   
        cursor = self.db.cursor()
        sql="select * from production where Batch_No = %s"
        values = (Batch_No,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
    
    def update(self, values):
        cursor = self.db.cursor()
        sql= "update production set API_Particle_Size=%s, Screen_Size=%s, Blend_Time=%s, Compressor=%s, Inlet_Temp=%s, Spray_Rate=%s, Dissolution%s where Batch_No = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, Batch_No):
        cursor = self.db.cursor()
        sql="delete from production where Batch_No = %s"
        values = (Batch_No,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

ProductionDAO = ProductionDAO()