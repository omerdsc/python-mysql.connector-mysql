import mysql.connnector
from datatime import datatime
from connection import connection
from student import student
from teacher import teacher

class DbManager:
    def __init__(self):
        self.conection=connection
        self.cursor=self.connection.cursor()

    def getStudentById(self,id):
        sql="select * from student where id=%s"
        values=(id,)
        self.cursor.execute(sql,values)
        
        try:
            obj=self.cursor.fetchone()
            return student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6])
        except mysql.connector.Erroe as err:
            print("hata",err)
    
    def getStudentByClassId(self,id):
        pass

    def addStudent(self,student:student):
        pass

    def editStudent(self,student:student):
        pass

    def addTeacher(self,teacher:teacher):
        pass

    def editTeacher(self,teacher:teacher):
        pass 


db=DbManager()

student=db.getStudentById(7)
print(student.name)
print(student.surname)

