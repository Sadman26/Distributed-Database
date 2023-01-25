import psycopg2
connection=psycopg2.connect(database='bubtlab',password='sad@2600',user='postgres')
cursor=connection.cursor()
#Create
def create():
    cursor.execute("INSERT INTO person (name, age) VALUES ('Sadman',22)")
    connection.commit()
    connection.close()
#Read
def read():
    cursor.execute("SELECT * FROM person;")
    print(cursor.fetchall())
    connection.close()
#Update
def update():
    cursor.execute("UPDATE person SET age=24 WHERE name='Sadman'")
    connection.commit()
    connection.close()
#Delete
def delete():
    cursor.execute("DELETE FROM person WHERE name='Sadman'")
    connection.commit()
    connection.close()
x=input("Enter your choice: ")
if x=='1':
    create()
elif x=='2':
    read()
elif x=='3':
    update()
elif x=='4':
    delete()