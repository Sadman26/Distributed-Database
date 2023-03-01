from pymongo import MongoClient
from bson.objectid import ObjectId
#?initialization
client=MongoClient('localhost' , 27017)
c=client['test']
db=c['person']
#Create
def insert():
    name=input('Enter name: ')
    age=input('Enter age: ')
    db.insert_one({'name':name,'age':age})
    print('Data inserted successfully')
#Update
def update():
    id=input('Enter id: ')
    name=input('Enter name: ')
    age=input('Enter age: ')
    db.update({'_id':ObjectId(id)},{'$set':{'name':name,'age':age}})
    print('Data updated successfully')
#Delete
def delete():
    id=input('Enter id: ')
    db.remove({'_id':ObjectId(id)})
    print('Data deleted successfully')
#Read
def findall():
    for i in db.find():
        print(i)
#Main function
def main():
    while True:
        print('=====CRUD=====')
        print('1. Create')
        print('2. Read')
        print('3. Update')
        print('5. Delete')
        print('6. Exit')
        choice=input('Enter your choice: ')
        if choice=='1':
            insert()
        elif choice=='2':
            findall()
        elif choice=='3':
            update()
        elif choice=='5':
            delete()
        elif choice=='6':
            break
        else:
            print('Invalid choice')
main()