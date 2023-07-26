# database_operations.py

import sqlite3

def connect_to_database():
    connection = sqlite3.connect('example.db')
    return connection

def create_table():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')
    connection.commit()
    connection.close()

def insert_into_table(date, trans, symbol, qty, price):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO stocks VALUES ('{date}', '{trans}', '{symbol}', {qty}, {price})")
    connection.commit()
    connection.close()

def select_from_table():
    connection = connect_to_database()
    cursor = connection.cursor()
    for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
    connection.close()

create_table()
insert_into_table('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
select_from_table()
