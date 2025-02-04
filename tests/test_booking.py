import unittest
from unittest.mock import patch, MagicMock
from app.database.booking import Booking

class TestBooking(unittest.TestCase):
    #mocking the get_db_connection function
    @patch('app.booking.get_db_connection')
    def test_create_table(self, mock_get_db_connction):
        mock_conn = MagicMock()
        mock_get_db_connction.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        Booking.create_table()

        mock_cursor.execute.assert_called_once_with('''
                    CREATE TABLE IF NOT EXISTS bookings (
                       booking_reference TEXT PRIMARY KEY,
                       customer_id INTEGER NOT NULL,
                       checkin_date DATE NOT NULL,
                       checkout_date DATE NOT NULL,
                       room_number INT NOT NULL)''')
        
        mock_conn.commit.assert_called()
        mock_conn.close.assert_called()

    
    def test_create_new_booking(self):
        booking = Booking(1, 1, '2024-01-01', '2024-03-03', 101)
        self.assertEqual(booking.booking_reference, 1)
        self.assertEqual(booking.customer_id, 1)
        self.assertEqual(booking.checkin_date, '2024-01-01')
        self.assertEqual(booking.checkout_date, '2024-03-03')
        self.assertEqual(booking.room_number, 101)