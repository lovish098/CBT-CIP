import pymysql


print("Welcome to Phone Directory")

conn = pymysql.connect(host='localhost',user='root',password='root',database='phonebook')
def mysqlcon(name, number, text):
    cursor = conn.cursor()
    insert_query = 'INSERT INTO contactlist (name, number, text) VALUES (%s, %s, %s)'
    data = (name, number, text)
    cursor.execute(insert_query, data)
    conn.commit()
    print("Data entered successfully")
    cursor.close()
    

def mysqlshow():
    cursor = conn.cursor()
    cursor.execute( 'SELECT * FROM contactlist')
    row=cursor.fetchall()
    for i in row:
       print(i)
    
def mysqldel(name):
   cursor = conn.cursor()
   delete_query = 'DELETE FROM contactlist WHERE name=%s'
   data = (name)
   cursor.execute(delete_query, data)
   conn.commit()
   print("Data deleted successfully")
   cursor.close()


def mysqlsrc(name):
   cursor = conn.cursor()
   srch_query = 'SELECT * FROM contactlist WHERE name=%s'
   data = (name)
   cursor.execute(srch_query, data)
   conn.commit()
   print("Data searched successfully")
   results = cursor.fetchall()
   if results:
        print("Search Results:")
        for row in results:
            print(row)
   cursor.close()

print("Enter a for add new contact \nEnter d for delete contact \nEnter s for see all contacts \nEnter q for search contacts")

user=input()

if user == 'a':
  name = input("Enter name:")
  number = input("Enter number:")
  text = input("Enter text:")
  mysqlcon(name, number, text)

elif user == 's':
    mysqlshow()

elif user == 'd':
    name=input("enter name:")
    mysqldel(name)
elif user == 'q':
    name=input("Enter name:")
    mysqlsrc(name)
else: 
   print("error")

conn.close()