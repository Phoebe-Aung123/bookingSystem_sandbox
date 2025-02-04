import sqlite3

def get_db_connection():
    conn = sqlite3.connect('booking.db')
    
    return conn



        

