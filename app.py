import psycopg2
connection=psycopg2.connect(user="postgres",password="sad@2600",port="5432",database="bubtlab")
connection.autocommit=True
cursor=connection.cursor()
sql = '''copy omg from 'E:\DDB\data.csv' delimiter ',' csv header;'''
cursor.execute(sql)
connection.commit()
cursor.close()
#just some comment