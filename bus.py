class Bus:
    def __init__(self, bcode, bus_name, seat, booked, depart_time, arrival_time):
        self.bcode = bcode
        self.bus_name = bus_name
        self.seat = seat
        self.booked = booked
        self.depart_time = depart_time
        self.arrival_time = arrival_time
        self.next = None

    def display(self):
        print("{:<6} | {:<8} | {:<4} | {:<6} | {:<11} | {:<12} | {:<11}".format(
            self.bcode, self.bus_name, self.seat, self.booked, self.depart_time, self.arrival_time,
            self.arrival_time - self.depart_time
        ))
