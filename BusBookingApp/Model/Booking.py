class Booking:
    def __init__(self, bcode, ccode, seat):
        self.bcode = bcode
        self.ccode = ccode
        self.seat = seat
    def __str__(self):
        return f"{self.bcode}, {self.ccode}, {self.seat}"