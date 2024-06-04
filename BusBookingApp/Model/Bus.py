class Bus:
    def __init__(self, bcode, bus_name, seat, booked, depart_time, arrival_time):
        self.bcode = bcode
        self.bus_name = bus_name
        self.seat = seat
        self.booked = booked
        self.depart_time = depart_time
        self.arrival_time = arrival_time
    def __str__(self):
        return f"{self.bcode}, {self.bus_name}, {self.seat}, {self.booked}, {self.depart_time}, {self.arrival_time}"
    def is_valid(self):
        return self.seat > 0 and 0 <= self.booked <= self.seat and self.arrival_time > self.depart_time