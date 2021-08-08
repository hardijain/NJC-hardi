import sqlite3
connection=sqlite3.connect('Movies.db')
cursor=connection.cursor()


command1=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cursor.execute(command1)


cursor.execute(" INSERT INTO Movies VALUES ('Sholay','Amitabh Bachchan','Hema Malini','Ramesh Sippy',1975)")
cursor.execute(" INSERT INTO Movies VALUES ('Don','Amitabh Bachchan','Zeenat Aman','Chandra Barot',1978)")
cursor.execute(" INSERT INTO Movies VALUES ('Lagaan','Amir Khan','Gracy Singh','Ashutosh Gowariker',2001)")
cursor.execute(" INSERT INTO Movies VALUES ('Raazi','Vicky kaushal','Alia Bhatt','Meghna Gulzar',2018)")



cursor.execute("SELECT * FROM Movies")
results=cursor.fetchall()


cursor.execute("SELECT * FROM Movies WHERE actor='Amitabh Bachchan' ")
results2=cursor.fetchall()

#print the results
print(results)

print(results2)