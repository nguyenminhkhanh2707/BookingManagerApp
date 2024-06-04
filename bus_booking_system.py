from bus import Bus

class BusBookingSystem:
    def __init__(self):
        self.bus_head = None

    def load_bus_data_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split('|')
                    bcode, bus_name, seat, booked, depart_time, arrival_time = data
                    new_bus = Bus(bcode.strip(), bus_name.strip(), int(seat), int(booked), float(depart_time), float(arrival_time))
                    self.add_bus(new_bus)
            print("Bus data loaded successfully from file.")
        except FileNotFoundError:
            print("File not found. No data loaded.")

    def add_bus(self, new_bus):
        if not self.bus_head:
            self.bus_head = new_bus
        else:
            new_bus.next = self.bus_head
            self.bus_head = new_bus

    def display_all_buses(self):
        if not self.bus_head:
            print("No buses found.")
            return
        current = self.bus_head
        print("{:<6} | {:<8} | {:<4} | {:<6} | {:<11} | {:<12} | {:<11}".format(
            "bcode", "bus_name", "seat", "booked", "depart_time", "arrival_time", "travel_time"
        ))
        print("-" * 75)
        while current:
            current.display()
            current = current.next

    def save_all_buses_to_file(self, filename):
        if not self.bus_head:
            print("No buses found to save.")
            return
        try:
            with open(filename, 'w') as file:
                current = self.bus_head
                while current:
                    file.write("{:<6} | {:<8} | {:<4} | {:<6} | {:<11} | {:<12}\n".format(
                        current.bcode, current.bus_name, current.seat, current.booked, current.depart_time, current.arrival_time
                    ))
                    current = current.next
            print("Bus data saved to file successfully.")
        except:
            print("Error occurred while saving data to file.")

    def search_bus_by_bcode(self, bcode):
        if not self.bus_head:
            print("No buses found.")
            return
        current = self.bus_head
        while current:
            if current.bcode == bcode:
                print("Bus found:")
                current.display()
                return
            current = current.next
        print("Bus with bcode {} not found.".format(bcode))

    def delete_bus_by_bcode(self, bcode):
        if not self.bus_head:
            print("No buses found.")
            return
        if self.bus_head.bcode == bcode:
            self.bus_head = self.bus_head.next
            print("Bus with bcode {} deleted successfully.".format(bcode))
            return
        prev = None
        current = self.bus_head
        while current:
            if current.bcode == bcode:
                prev.next = current.next
                print("Bus with bcode {} deleted successfully.".format(bcode))
                return
            prev = current
            current = current.next
        print("Bus with bcode {} not found.".format(bcode))

    def sort_buses_by_bcode(self):
        if not self.bus_head:
            print("No buses found to sort.")
            return
        buses = []
        current = self.bus_head
        while current:
            buses.append(current)
            current = current.next
        buses.sort(key=lambda x: x.bcode)
        self.bus_head = buses[0]
        current = self.bus_head
        for bus in buses[1:]:
            current.next = bus
            current = current.next
        current.next = None

    def add_bus_before_position(self, new_bus, k):
        if k < 0:
            print("Invalid position. Position should be non-negative.")
            return
        if k == 0:
            new_bus.next = self.bus_head
            self.bus_head = new_bus
            print("Bus added successfully at position {}.".format(k))
            return
        count = 0
        prev = None
        current = self.bus_head
        while current and count < k:
            prev = current
            current = current.next
            count += 1
        if count == k:
            new_bus.next = current
            prev.next = new_bus
            print("Bus added successfully at position {}.".format(k))
        else:
            print("Position {} exceeds the length of the list.".format(k))

    def delete_node_before_bcode(self, bcode):
        if not self.bus_head or not self.bus_head.next:
            print("No nodes to delete.")
            return
        if self.bus_head.next.bcode == bcode:
            self.bus_head = self.bus_head.next
            print("Node before bcode {} deleted successfully.".format(bcode))
            return
        prev = self.bus_head
        current = prev.next
        while current:
            if current.bcode == bcode:
                prev.next = current.next
                print("Node before bcode {} deleted successfully.".format(bcode))
                return
            prev = current
            current = current.next
        print("Node before bcode {} not found.".format(bcode))
