from .connection import get_db_connection

class Room:
    def __init__(self, room_number, capacity, availability):
        self.room_number = room_number
        self.capacity = capacity
        self.availability = availability

    def create_table():
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS rooms (
                       room_number INTEGER PRIMARY KEY,
                       availability CHAR,
                       capacity INTEGER NOT NULL)''')
        
        cursor.executemany(''' INSERT OR IGNORE INTO rooms (
                       room_number, availability, capacity) 
                       VALUES (?, ?, ?)''', [
                       (101, 'available', 2),
                       (102, 'available', 3),
                       (103, 'available', 2),
                       (104, 'available', 4),
                       (105, 'available', 2),
                       (106, 'available', 3) ])
        
        conn.commit()
        conn.close()


    def get_available_rooms():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(''' SELECT * FROM rooms 
                       WHERE availability = 'available'
                       ''')
        
        available_rooms = cursor.fetchall()

        #check if there are available rooms
        if not available_rooms: 
            print("There are no available rooms at the moment. ")
        else: 
            print("Room Number | Capacity | Availability")
            for room in available_rooms:
                print(f"    {room[0]}     |     {room[1]}    | {room[2]}")

        conn.commit()
        conn.close()

    def change_to_unavailable(room_num):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE rooms
                        SET availability = 'booked'
                        WHERE room_number = ?
                        ''', (room_num, ))
        
        conn.commit()
        conn.close()

    def change_to_available(room_num):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
                        UPDATE rooms
                        SET availability = 'available'
                        WHERE room_number = ?
                        ''', (room_num, ))
        
        conn.commit()
        conn.close()