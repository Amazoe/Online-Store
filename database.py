from asyncio.windows_events import NULL
import sqlite3
import csv

def Templete():
    conn = sqlite3.connect('items.db')
    cur = conn.cursor()
    
    #
    
    conn.commit()
    conn.close()

def CreateTable():
    conn = sqlite3.connect('items.db')
    cur = conn.cursor()
    
    cur.execute("DROP TABLE items")
    cur.execute("CREATE TABLE IF NOT EXISTS items(ProductID INT  , ProductName TEXT, Product_desc str , Price float)")
    
    conn.commit()
    conn.close()
    
def AddOne():
    conn = sqlite3.connect('items.db')
    cur = conn.cursor()
    
    x = (1111, 'test name', 'test description', 99.99)
    print(x)
    cur.execute("INSERT INTO items VALUES ",x)
    
    conn.commit()
    conn.close()
    
def AddMany():
    conn = sqlite3.connect('items.db')
    cur = conn.cursor()
    
    file = open("Online Store Project Items for Sale.csv", newline='')

    reader = csv.reader(file)
    header = next(reader)
    data = [row for row in reader]
    
    for i in range(len(data)):
        
        cur.execute("INSERT INTO items VALUES(?,?,?,?)", ((data[i][0]),None,(data[i][1]),(data[i][2])))

    conn.commit()
    conn.close()

def ShowAll():
    conn = sqlite3.connect('items.db')
    cur = conn.cursor()
    
    cur.execute("SELECT rowid, * FROM items")
    items = cur.fetchall()
    
    for item in items:
        print(item)
    
    conn.commit()
    conn.close()


CreateTable()
#AddOne()
AddMany()
ShowAll()

