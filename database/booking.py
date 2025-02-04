from .connection import get_db_connection

class Booking: 
    def __init__(self, booking_reference, customer_id, checkin_date, checkout_date, room_number):
        self.booking_reference = booking_reference
        self.customer_id = customer_id
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.room_number = room_number

    def create_table():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS bookings (
                       booking_reference TEXT PRIMARY KEY,
                       customer_id INTEGER NOT NULL,
                       checkin_date DATE NOT NULL,
                       checkout_date DATE NOT NULL,
                       room_number INT NOT NULL)''')
        
        conn.commit()
        conn.close()

    def create_new_booking(reference, customer_id, checkin, checkout, room_number):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO bookings (booking_reference, customer_id, checkin_date, checkout_date, 
                       room_number)
                       VALUES (?, ?, ?, ?, ?)''', (reference, customer_id, checkin, checkout, room_number))
    
        conn.commit()
        conn.close()




