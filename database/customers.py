from .connection import get_db_connection
from random import randint

class Customer:
    def __init__(self, customer_id, first_name, last_name, age):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def create_table():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS customers (
                       customer_id INTEGER PRIMARY KEY,
                       first_name TEXT NOT NULL,
                       last_name TEXT NOT NULL,
                       gmail TEXT NOT NULL,
                       age INTEGER NOT NULL)''')
        conn.commit()
        conn.close()

    def create_new_customer(first_name, last_name, gmail, age):
        
        conn = get_db_connection()
        cursor = conn.cursor()

        #get the highest customer_id in the database
        cursor.execute('''SELECT MAX(customer_id) FROM customers''')
        max_id = cursor.fetchone()


        if max_id[0] is None: 
            customer_id = 1001
        else:
            customer_id = max_id[0] + 1

        cursor.execute('''
                       INSERT INTO customers (customer_id, first_name, last_name, gmail, age)
                       VALUES (?, ?, ?, ?, ?)''', (customer_id, first_name, last_name, gmail, age))
        
 
        conn.commit()
        conn.close()

        return customer_id
    
    def get_customer_details(gmail): 
        conn = get_db_connection()
        cursor = conn.cursor()

        customer_id = cursor.execute("SELECT customer_id WHERE gmail = ?", gmail)

        conn.commit()
        conn.close()

        return customer_id