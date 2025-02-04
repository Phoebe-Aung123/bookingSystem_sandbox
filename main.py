from datetime import datetime
from database.connection import get_db_connection
from database.rooms import Room
from database.customers import Customer
from database.booking import Booking
from random import randint
import sys
from sqids import Sqids

Customer.create_table()
Room.create_table()
Booking.create_table()

date_format = '%d/%m/%Y'

def get_customer_details():
    first_name = input("Enter your first name: ")

    last_name = input("Enter your last name: ")

    gmail = input('Enter your gmail: ')

    age = int(input("Enter your age: "))

    return first_name, last_name, gmail, age

def get_booking_details():
    while True:
        try:
            check_in_date = input("Check-in date (dd/mm/YYYY): ")
            check_out_date = input("Check-out date (dd/mm/YYYY): ")

            check_in_date_obj = datetime.strptime(check_in_date, date_format).date()
            check_out_date_obj = datetime.strptime(check_out_date, date_format).date()

            if check_in_date_obj > check_out_date_obj: 
                print("Please enter a valid date range. Check-in date should be before check-out date.")

            else: 
                return check_in_date_obj, check_out_date_obj

        except ValueError:
            print("Please enter a valid date format (dd/mm/YYYY): ")

def generate_reference_number(customer_id, rand_id): 
    sqids = Sqids(alphabet = "abcdefghijkmnpqrtuvwxyzABCDEFGHJKLMNPQRTUVWXYZ2346789", min_length = 8)
    id = sqids.encode([customer_id, rand_id])
    return id
           

def main():

    print("Are a new customer or existing customer?")

    customer_type = input("Enter 'N' for new and 'E' for existing customer: ")

    if customer_type.lower() == 'n':
        #get customer details
        first_name, last_name, gmail, age = get_customer_details()
        #create new customer in the database
        customer_id = Customer.create_new_customer(first_name, last_name, gmail, age)
    else:
        gmail = input("Enter your gmail: ")
        customer_id = Customer.get_customer_details(gmail)

    #get booking dates 
    check_in_date, check_out_date = get_booking_details()

    print("\n")

    #display available rooms
    available_rooms = Room.get_available_rooms()

    print("\n")

    #asks if the user wants to continue with the booking 
    to_proceed = input("Would you like to proceed with the booking? Enter Y/N: ")

    #error handling for invalid input 
    while True: 
        if to_proceed.lower() not in ['y', 'n']:
            print("Invalid input. Please enter Y/N.")
            to_proceed = input("Would you like to proceed with the booking? Enter Y/N: ")
        else:
            break

    #get the room number to book from the user if the user wants to proceed
    if to_proceed.lower() == 'y':
        room_to_book = int(input("Enter the room number you would like to book: "))
        #change the room avaialbility
        Room.change_to_unavailable(room_to_book)
    else: 
        print("Thank you for visiting.")
        sys.exit()   

    rand_num = randint(1, 1000)

    #generate booking reference
    reference_id = generate_reference_number(customer_id, rand_num)

    #create new booking in the database
    Booking.create_new_booking(reference_id, customer_id, check_in_date, check_out_date, room_to_book)

    #display booking confirmation 
    print("Your booking has been successfully created. Find your booking details below:\n ")
    print(f"Booking reference number: {reference_id}")
    print(f"Customer_id: {customer_id}")
    print(f"First name: {first_name}             Last name: {last_name}")
    print(f"Checkin Date: {check_in_date}        Checkout Date: {check_out_date}")




if __name__ == "__main__":
    main()