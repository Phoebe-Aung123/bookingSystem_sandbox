Booking System 

A simple booking system for managing customer reservations and room bookings. It includes customer management (creating new customers and retrieving customer detials), room management, and booking creation. This system uses SQLite for database storage. 

Available Funcions: 
--> create_new_booking(reference, customer_id, checkin, checkout, room_number): adds a new data entry in the booking table

--> create_new_customer(first_name, last_name, gmail, age): adds a new customer in the customer table. The customer is id is also auto-generated in this function based on the number of customers

--> get_customer_details(gmail): retrived the details of an exisiting customer based on his/her gmail. It returns their first_name, last_name, and age

--> get_available_rooms(): retrieves the rooms available to book, returns the room number, capacity, and availability

--> change_to_unavailable(room_num): changes the availability of a room to 'booked' after the customer confirms booking.

HOW TO GET STARTED: 
1. Choose whether you are an exisiting customer or a new customer. (choose new)
2. Enter your details, including your first name, last name, email, and age. Customer_id will be generated for you. 
3. The system will ask for your booking details: checkin and checkout date. 
4. It will provide the user with a list of available rooms within that period.
5. Enter 'y' to proceed with the booking and 'n' to exit the system.
6. Choose one of the available room numbers shown before to book.
7. The system will display the booking detials including the reference number, cusotmer_id, first_name, last_name, checkin date, and checkout date