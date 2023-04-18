# qustion 1
import sqlite3
con=sqlite3.connect("1.db")
cur=con.cursor()
def tbl(): # Create a Table
    cur.execute(''' CREATE TABLE shop(customer_id,customer_name,city,Phone_no)''')
    con.commit()
    return app()
def data():
    print("List of tables are")
    for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        print("---",row[0])
    
    tab_name = str(input("Enter table to add data: "))
    cus_id = '''SELECT MAX(customer_id) FROM {0}'''.format(tab_name)
    cur.execute(cus_id)
    max_cus_id = cur.fetchall()
    for i in max_cus_id:
        max_cus_id = int(max(i))+ 1
    name = str(input("Enter customer name: "))
    place = str(input("Enter customer city: "))
    contact = str(input("Enter customer contact number: "))
    cmd = ''' INSERT INTO shop VALUES ({0},'{1}','{2}',{3})'''.format(max_cus_id,name,place,contact)
    cur.execute(cmd)
    con.commit()
    return app()
def srtid(): # to sort by id
    for row in cur.execute(''' SELECT * FROM shop ORDER BY customer_id DESC '''):
        print(row)
    return app()
def lstcust(): # to list Customer names
    cus_name = str(input("Enter Customer name: "))
    cmd = ''' SELECT * FROM shop WHERE customer_name='{0}'  '''.format(cus_name)
    for row in cur.execute(cmd):
        print(row)
    return app()
def lstcusbycity():
    city = str(input("Enter customer city: "))
    cmd = ''' SELECT customer_name FROM shop WHERE city='{0}'  '''.format(city)
    for row in cur.execute(cmd):
        print(row)
    return app()
def rmcust():
    del_cust = str(input("Enter customer name to remove: "))
    cmd = ''' DELETE FROM shop WHERE customer_name='{0}'  '''.format(del_cust)
    cur.execute(cmd)
    con.commit()
    for i in cur.execute(''' SELECT * FROM shop '''):
        print(i)
    return app()
def lst():
    cur.execute(''' SELECT * FROM shop ''')
    for row in cur:
        print(row)
    return app()
def app():
    print('''
            Press 1 = Create Table
            Press 2 = Add Data
            Press 3 = Sort data By Id
            Press 4 = List Customer by City
            Press 5 = List the Specific Customer
            Press 6 = Remove Specific Customer
            Press 7 = List All Customers
            Press 0 = Exit''')
    op=int(input("Select the Option : "))
    if(op==1):
        return tbl()
    elif(op==2):
        return data()
    elif(op==3):
        return srtid()
    elif(op==4):
        return lstcusbycity()
    elif(op==5):
        return lstcust()
    elif(op==6):
        return rmcust()
    elif(op==7):
        return lst()
    elif(op==0):
        con.close()
        print("Bye have a Good Day")
        return exit
    else:
        print("Retry..")
        return app()
app()
    
