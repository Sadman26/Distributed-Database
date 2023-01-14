import psycopg2
connection=psycopg2.connect(user="postgres",password="sad@2600",port="5432",database="bubtlab")
connection.autocommit=True
cursor=connection.cursor()
sql2 = '''copy omg
from 'E:\DDB\data.csv'
delimiter ','
csv header;'''
cursor.execute(sql2)
connection.commit()
cursor.close()