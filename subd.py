import sqlite3
conn = sqlite3.connect('movie.db')
# CRUD- CREATE READ UPDATE DELETE
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS films(
title TEXT NOT NULL,
age INT NOT NULL,
author TEXT NOT NULL
)''')

cursor.execute('''INSERT INTO 
films (title, age, author)
 VALUES ('наруто',1998,'kisimoto')''')



conn.commit()
