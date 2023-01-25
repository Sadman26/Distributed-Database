import psycopg2
connection=psycopg2.connect(database='bubtlab',password='sad@2600',user='postgres')
cursor=connection.cursor()
#Create
def create():
    x=input('Enter Name: ')
    y=input('Enter Age: ')
    cursor.execute("INSERT INTO person(name,age) VALUES(%s,%s)",(x,y))
    connection.commit()
    connection.close()
#Read
def read():
    cursor.execute('SELECT count(*) FROM person;')
    for i in cursor:
        print(i[0],' Data Available')
    cursor.execute("SELECT * FROM person;")
    for i in cursor:
        print('=======================')
        print('Name: ',i[1])
        print('Age: ',i[2])
        print('=======================')
    connection.close()
#Update
def update():
    x=input('UPDATE : ')
    xx=input('Which Data you want to Update : ')
    if(xx=='1'):
        xx1=input('Enter New Name: ')
        cursor.execute("UPDATE person SET name=%s WHERE name=%s",(xx1,x,))
        connection.commit()
        if(connection):
            print('Updated Name')
        connection.close()
    elif(xx=='2'):
        xx1=input('Enter New Age: ')
        cursor.execute("UPDATE person SET age=%s WHERE name=%s",(xx1,x,))
        connection.commit()
        if(connection):
            print('Updated Name')
        connection.close()
#Delete
def delete():
    x=input('DELETE : ')
    cursor.execute("DELETE FROM person WHERE name=%s",(x,))
    connection.commit()
    if(connection):
        print('Deleted Data')
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