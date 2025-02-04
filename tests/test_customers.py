import unittest
from unittest.mock import patch, MagicMock
from app.database.customers import Customer

class TestBooking(unittest.TestCase):
    #mocking the get_db_connection function
    @patch('app.database.customers.get_db_connection')
    def test_create_table(self, mock_get_db_connction):
        mock_conn = MagicMock()
        mock_get_db_connction.return_value = mock_conn
        mock_cursor = mock_conn.cursor.return_value

        Customer.create_table()

        mock_cursor.execute.assert_called_once_with('''
                       CREATE TABLE IF NOT EXISTS customers (
                       customer_id INTEGER PRIMARY KEY,
                       first_name TEXT NOT NULL,
                       last_name TEXT NOT NULL,
                       gmail TEXT NOT NULL,
                       age INTEGER NOT NULL)''')
        
        mock_conn.commit.assert_called()
        mock_conn.close.assert_called()

    @patch('app.database.customers.get_db_connection')
    def test_create_new_customers_empty_table(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_get_db_connection.return_value = mock_conn 
        mock_cursor = mock_conn.cursor.return_value

        mock_cursor.fetchone.return_value = (None, )

        first_name = "Bruno"
        last_name = "Mars"
        gmail = "bruno@gmail.com"
        age = 40

        customer_id = Customer.create_new_customer(first_name, last_name, gmail, age)

        self.assertEqual(customer_id, 1001)

        mock_cursor.execute.assert_any_call('''
                       INSERT INTO customers (customer_id, first_name, last_name, gmail, age)
                       VALUES (?, ?, ?, ?, ?)''', (1001, first_name, last_name, gmail, age))
        
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()

    @patch('app.database.customers.get_db_connection')
    def test_create_new_customers_non_empty_table(self, mock_get_db_connection):
        mock_conn = MagicMock()
        mock_get_db_connection.return_value = mock_conn 
        mock_cursor = mock_conn.cursor.return_value

        mock_cursor.fetchone.return_value = (1003, )

        first_name = "Bruno"
        last_name = "Mars"
        gmail = "bruno@gmail.com"
        age = 40

        customer_id = Customer.create_new_customer(first_name, last_name, gmail, age)
        
        #check that the returned customer id is 1004
        self.assertEqual(customer_id, 1004)
        
        mock_cursor.execute.assert_any_call('''
                       INSERT INTO customers (customer_id, first_name, last_name, gmail, age)
                       VALUES (?, ?, ?, ?, ?)''', (1004, first_name, last_name, gmail, age))
        

        
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()