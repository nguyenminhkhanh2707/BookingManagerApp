class Customer:
    def __init__(self, ccode, name, phone):
        self.ccode = ccode
        self.name = name
        self.phone = phone
    def __str__(self):
        return f"{self.ccode}, {self.name}, {self.phone}"