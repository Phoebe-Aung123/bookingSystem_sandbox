import unittest
from unittest.mock import patch, MagicMock
from app.database.rooms import Room

class TestRooms(unittest.TestCase):
    #mocking the get_db_connection function
    @patch('app.database.rooms.get_db_connection')
    def test_create_table(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        Room.create_table()
        mock_cursor.execute.assert_called_once_with('''
                    CREATE TABLE IF NOT EXISTS rooms (
                       room_number INTEGER PRIMARY KEY,
                       availability CHAR,
                       capacity INTEGER NOT NULL)''')
        
        mock_cursor.executemany.assert_any_call(''' INSERT OR IGNORE INTO rooms (
                       room_number, availability, capacity) 
                       VALUES (?, ?, ?)''', [
                       (101, 'available', 2),
                       (102, 'available', 3),
                       (103, 'available', 2),
                       (104, 'available', 4),
                       (105, 'available', 2),
                       (106, 'available', 3) ])
        
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('builtins.print')
    @patch('app.database.rooms.get_db_connection')
    def test_get_avaialable_rooms(self, mock_get_db_connection, mock_print):
        mock_conn = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        mock_cursor.fetchall.return_value = [
                       (101, 2, 'available'),
                       (102, 3, 'available')]
        
        Room.get_available_rooms()

        mock_print.assert_any_call("Room Number | Capacity | Availability")
        mock_print.assert_any_call("    101     |     2    | available")
        mock_print.assert_any_call("    102     |     3    | available")

        mock_cursor.execute.assert_called_once_with(''' SELECT * FROM rooms 
                       WHERE availability = 'available'
                       ''')
        
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('app.database.rooms.get_db_connection')
    def test_change_to_unavailable(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_get_db_connection.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value
        
        room_num = 101

        Room.change_to_unavailable(room_num)

        mock_cursor.execute.assert_any_call('''
                        UPDATE rooms
                        SET availability = 'booked'
                        WHERE room_number = ?
                        ''', (room_num, ))
        
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

        

