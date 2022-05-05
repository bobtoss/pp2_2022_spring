import psycopg2
import re

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='alma45884'
)
current = config.cursor()
postgres_select_query = """SELECT * FROM phonebook"""
current.execute(postgres_select_query)
result = current.fetchall()
s=input("in what collumn you want to search pattern? : ")
pattern=input('write down your pattern : ')
if s=="username":
    for i in range(len(result)):
        c=result[i][0]
        if re.findall(pattern,c):
            sql= result[i]

else:
    for i in range(len(result)):
        c=result[i][1]
        if re.findall(pattern,c):
            sql= result[i]
print(sql)

config.commit()
current.close()
config.close()