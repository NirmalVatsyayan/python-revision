import psycopg2

from termcolor import colored
import sys


def get_connection():
    try:
        conn = psycopg2.connect("dbname='test' user='postgres' host='localhost' password='postgres'")
        print (colored("I am connected to database", "green"))
    except:
        print (colored("I am unable to connect to the database","red"))
        sys.exit(1)

    return conn

def close_connection(conn):
    conn.close()

def get_version():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('SELECT version()')          
    ver = cur.fetchone()
    print("Printing version ---->>>>  ",ver)
    for data in ver:
        print(data)
    close_connection(conn)
    

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    
    conn.commit()
    close_connection(conn)

def drop_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Cars")

    conn.commit()
    close_connection(conn)


def insert_values():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
    
    conn.commit()
    close_connection(conn)

def insert_many():
    conn = get_connection()
    cur = conn.cursor()

    cars = (
        (9, 'Audi1', 52642),
        (10, 'Mercedes1', 57127),
        (12, 'Skoda1', 9000),
        (13, 'Volvo1', 29000),
        (14, 'Bentley1', 350000),
        (15, 'Citroen1', 21000),
        (16, 'Hummer1', 41400),
        (17, 'Volkswagen1', 21600)
    )
    query = "INSERT INTO Cars (Id, Name, Price) VALUES (%s, %s, %s)"
    cur.executemany(query, cars)

    conn.commit()
    close_connection(conn)
 
def purge_data():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    close_connection(conn)

def update_data():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("UPDATE Cars SET price=10000 where id=1")
    conn.commit()
    close_connection(conn)

def delete_data():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("DELETE from Cars where id=8")
    conn.commit()
    close_connection(conn)

'''
C - CREATE
R - READ
U - UPDATE
D - DELETE
'''

#get_version()        
#create_table()
#drop_table()

#insert_values()
#insert_many()

#purge_data()

#update_data()
#delete_data()


