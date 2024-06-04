from Model.MyCircularLinkedList import MyCircularLinkedList

class BookingRepository:
    def __init__(self):
        self.booking_list = MyCircularLinkedList()
    
    def getAll(self):
        return self.booking_list
    
    def setList(self, linked_list):
        self.booking_list = linked_list

    def addFirst(self, booking):
        self.booking_list.addFirst(booking)

    def addLast(self, booking):
        self.booking_list.addLast(booking)

    def isEmpty(self):
        return self.booking_list.isEmpty()
    
    def clear(self):
        self.booking_list.head = None