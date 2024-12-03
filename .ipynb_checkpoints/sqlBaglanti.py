import  mysql.connector

mydb=mysql.connector.connect(
    host="localhost", #192.23.45.46 internet üzerinden satın alırsak böyle bir şey yazarız şimdilik yerel server kullanıyoruz
    user="root",
    password="2121"
)

print(mydb)