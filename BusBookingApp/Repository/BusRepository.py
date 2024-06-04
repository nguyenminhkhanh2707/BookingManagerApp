from Model.MyCircularLinkedList import MyCircularLinkedList

class BusRepository:
    def __init__(self):
        self.bus_list = MyCircularLinkedList()
    
    def getAll(self):
        return self.bus_list
    
    def setList(self, linked_list):
        self.bus_list = linked_list

    def addFirst(self, bus):
        self.bus_list.addFirst(bus)

    def addLast(self, bus):
        self.bus_list.addLast(bus)

    def addBefore(self, position, bus):
        self.bus_list.addBefore(position, bus)

    def isEmpty(self):
        return self.bus_list.isEmpty()
    
    def delete(self, bus):
        self.bus_list.delete(bus)

    def search(self, xCode):
        for bus in self.getAll():
            if bus.bcode == xCode:
                return bus
        return None
    
    def searchBefore(self, xCode):
        prev_bus = None
        for bus in self.getAll():
            if bus.bcode == xCode:
                return prev_bus
            prev_bus = bus
        return None
    
    def clear(self):
        self.bus_list.head = None

    def update(self, old, new):
        self.bus_list.update(old, new)