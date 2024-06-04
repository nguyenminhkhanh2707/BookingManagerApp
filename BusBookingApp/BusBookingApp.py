from Service.BusService import BusService
from Service.CustomerService import CustomerService
from Service.BookingService import BookingService
from Repository.BusRepository import BusRepository
from Repository.CustomerRepository import CustomerRepository
from Repository.BookingRepository import BookingRepository
from Model.Bus import Bus
from Model.Customer import Customer
from Model.Booking import Booking

def displayBuses(buses):
    print("bcode | bus_name | seat | booked | depart_time | arrival_time | travel_time")
    print("-" * 71)

    for bus in buses:
        travel_time = round(bus.arrival_time - bus.depart_time, 1)
        print(f"{bus.bcode.ljust(5)} | {bus.bus_name.ljust(8)} | {str(bus.seat).ljust(4)} | {str(bus.booked).ljust(6)} | {str(bus.depart_time).ljust(11)} | {str(bus.arrival_time).ljust(12)} | {str(travel_time)}")

def displayCustomers(customers):
    print("ccode | name    | phone")
    print("-" * 26)

    for customer in customers:
        print(f"{customer.ccode.ljust(5)} | {customer.name.ljust(8)} | {customer.phone}")

def displayBookings(bookings, busService):
    for booking in bookings:
        bus = busService.search(booking.bcode)
        travel_time = round(bus.arrival_time - bus.depart_time, 1)
        print(f"Bus: {booking.bcode}, Customer: {booking.ccode}, Travel time: {travel_time}")

def bus_menu(busService):
    while True:
        print("\nBus Menu:")
        print("1. Load data from file")
        print("2. Input & add to the head")
        print("3. Display data")
        print("4. Save bus list to file")
        print("5. Search by bcode")
        print("6. Delete by bcode")
        print("7. Sort by bcode")
        print("8. Add before position k")
        print("9. Delete the node before the node having bcode = xCode")
        print("10. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_name = input("Enter file name: ")
            busService.loadData(file_name)
        elif choice == '2':
            bcode = input("Enter bus code: ")
            bus_name = input("Enter bus name: ")
            seat = int(input("Enter number of seats: "))
            booked = int(input("Enter number of booked seats: "))
            depart_time = float(input("Enter departure time: "))
            arrival_time = float(input("Enter arrival time: "))

            new_bus = Bus(bcode, bus_name, seat, booked, depart_time, arrival_time)
            if new_bus.is_valid() and not busService.isDuplicate(bcode):
                busService.addFirst(new_bus)
                print("Add bus successful.")
            else:
                print("Invalid input or duplicate bus code. Please enter again.")
        elif choice == '3':
            displayBuses(busService.getAll())
        elif choice == '4':
            file_name = input("Enter file name: ")
            busService.saveAs(file_name)
        elif choice == '5':
            bcode = input("Enter bus code to search: ")
            bus = busService.search(bcode)
            if bus != None:
                print("Bus found:", bus)
            else:
                print("Bus not found.")
        elif choice == '6':
            bcode = input("Enter bus code to delete: ")
            isDeleted = busService.dele(bcode)
            if isDeleted:
                print(f"Delete {bcode} success")
            else:
                print(f"Not found {bcode} to delete")
        elif choice == '7':
            busService.sortByBcode()
            print("Bus list sorted by bcode.")
        elif choice == '8':
            k = int(input("Enter position k: "))
            while k < 0:
                k = int(input("Invalid position. Please enter again: "))
            bcode = input("Enter bus code: ")
            bus_name = input("Enter bus name: ")
            seat = int(input("Enter number of seats: "))
            booked = int(input("Enter number of booked seats: "))
            depart_time = float(input("Enter departure time: "))
            arrival_time = float(input("Enter arrival time: "))

            new_bus = Bus(bcode, bus_name, seat, booked, depart_time, arrival_time)
            if new_bus.is_valid() and not busService.isDuplicate(bcode):
                busService.addBefore(k, new_bus)
                print("Add bus successful.")
            else:
                print("Invalid input or duplicate bus code. Please enter again.")         
        elif choice == '9':
            xCode = input("Enter bus code: ")
            busService.deleteBefore(xCode)
        elif choice == '10':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def customer_menu(customerService):
    while True:
        print("\nCustomer Menu:")
        print("1. Load data from file")
        print("2. Input & add to the end")
        print("3. Display data")
        print("4. Save customer list to file")
        print("5. Search by ccode")
        print("6. Delete by ccode")
        print("7. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_name = input("Enter file name: ")
            customerService.loadData(file_name)
        elif choice == '2':
            ccode = input("Enter customer code: ")
            cus_name = input("Enter customer name: ")
            phone = input("Enter phone number: ")

            new_customer = Customer(ccode, cus_name, phone)

            if not customerService.isDuplicate(ccode):
                customerService.addLast(new_customer)
                print("Add successful")
            else:
                print("Add fail. Please try again")
        elif choice == '3':
            displayCustomers(customerService.getAll())
        elif choice == '4':
            file_name = input("Enter file name: ")
            customerService.saveAs(file_name)
        elif choice == '5':
            ccode = input("Enter customer code to search: ")
            customer = customerService.search(ccode)
            if customer:
                print("Customer found:", customer)
            else:
                print("Customer not found.")
        elif choice == '6':
            ccode = input("Enter customer code to delete: ")
            if customerService.dele(ccode):
                print("Customer deleted successfully.")
            else:
                print("Customer not found.")
        elif choice == '7':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")

def booking_menu(bookingService, busService, customerService):
    while True:
        print("\nBooking Menu:")
        print("1. Input data")
        print("2. Display booking data width travel time")
        print("3. Sort by bcode + ccode")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            bus_code = input("Enter bus code: ")
            customer_code = input("Enter customer code: ")
            num_seats = int(input("Enter number of seats to be booked: "))

            bus = busService.search(bus_code)
            if bus is None:
                print("Bus code not found.")
                continue

            customer = customerService.search(customer_code)
            if customer is None:
                print("Customer code not found.")
                continue

            # Check if both bus and customer codes are already booked
            if bookingService.isExist(bus_code, customer_code):
                print("Booking already exists.")
                continue

            if bus.booked == bus.seat:
                print("The bus is exhausted.")
                continue

            available_seats = bus.seat - bus.booked
            if num_seats <= available_seats:
                new_booking = Booking(bus_code, customer_code, num_seats)
                bookingService.addLast(new_booking)

                bus.booked += num_seats
                busService.update(bus_code, bus)

                print("Booking successful.")
            else:
                print("Number of seats requested exceeds available seats.")
                continue
                       
        elif choice == '2':
            print("Booking data with travel time:")
            bookings = bookingService.getAll()
            displayBookings(bookings, busService)
        elif choice == '3':
            print("Sorting booking data by bcode + ccode.")
            bookingService.sort()
            print("Booking data sorted.")
        elif choice == '4':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    busService = BusService(BusRepository())
    customerService = CustomerService(CustomerRepository())
    bookingService = BookingService(BookingRepository())
    while True:
        print("\nMenu:")
        print("1. Bus Management")
        print("2. Customer Management")
        print("3. Booking Management")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bus_menu(busService)
        elif choice == '2':
            customer_menu(customerService)
        elif choice == '3':
            booking_menu(bookingService, busService, customerService)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
            
            class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def insert_between(x, y, p):
    new_node = Node(p)  # Tạo một nút mới chứa cấu trúc p

    # Liên kết nút mới với cấu trúc x
    new_node.prev = x
    new_node.next = y

    # Cập nhật liên kết với nút mới
    if x:
        x.next = new_node
    if y:
        y.prev = new_node

    return x  # Trả về cấu trúc x sau khi đã chèn

# Tạo các nút cho cấu trúc x
x1 = Node("A")
x2 = Node("B")
x3 = Node("C")
x1.next = x2
x2.prev = x1
x2.next = x3
x3.prev = x2

# Tạo các nút cho cấu trúc y
y1 = Node("D")
y2 = Node("E")
y3 = Node("F")
y1.next = y2
y2.prev = y1
y2.next = y3
y3.prev = y2

# Chèn cấu trúc p giữa x và y
p = "G"
result = insert_between(x2, y1, p)

# In kết quả sau khi chèn
current_node = result
while current_node:
    print(current_node.data)
    current_node = current_node.next