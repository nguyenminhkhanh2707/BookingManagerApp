from bus_booking_system import BusBookingSystem

def main():
    bbs = BusBookingSystem()

    while True:
        print("\nBus Booking System")
        print("1. Load Bus Data from File")
        print("2. Add Bus")
        print("3. Display All Buses")
        print("4. Save All Buses to File")
        print("5. Search Bus by Code")
        print("6. Delete Bus by Code")
        print("7. Sort Buses by Code")
        print("8. Add Bus Before Position")
        print("9. Delete Node Before bcode")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename: ")
            bbs.load_bus_data_from_file(filename)
        elif choice == '2':
            bcode = input("Enter bus code: ")
            bus_name = input("Enter bus name: ")
            seat = int(input("Enter number of seats: "))
            booked = int(input("Enter number of booked seats: "))
            depart_time = float(input("Enter departure time: "))
            arrival_time = float(input("Enter arrival time: "))
            new_bus = Bus(bcode, bus_name, seat, booked, depart_time, arrival_time)
            bbs.add_bus(new_bus)
        elif choice == '3':
            bbs.display_all_buses()
        elif choice == '4':
            filename = input("Enter filename to save: ")
            bbs.save_all_buses_to_file(filename)
        elif choice == '5':
            bcode = input("Enter bus code to search: ")
            bbs.search_bus_by_bcode(bcode)
        elif choice == '6':
            bcode = input("Enter bus code to delete: ")
            bbs.delete_bus_by_bcode(bcode)
        elif choice == '7':
            bbs.sort_buses_by_bcode()
            print("Buses sorted by code.")
        elif choice == '8':
            bcode = input("Enter bus code: ")
            bus_name = input("Enter bus name: ")
            seat = int(input("Enter number of seats: "))
            booked = int(input("Enter number of booked seats: "))
            depart_time = float(input("Enter departure time: "))
            arrival_time = float(input("Enter arrival time: "))
            new_bus = Bus(bcode, bus_name, seat, booked, depart_time, arrival_time)
            k = int(input("Enter position to add before: "))
            bbs.add_bus_before_position(new_bus, k)
        elif choice == '9':
            bcode = input("Enter bus code to delete node before: ")
            bbs.delete_node_before_bcode(bcode)
        elif choice == '0':
            print("Thank you for using the Bus Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
