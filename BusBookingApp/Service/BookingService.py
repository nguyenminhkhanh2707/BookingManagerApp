import csv
import os
from Model.Booking import Booking

class BookingService:
    def __init__(self, repo):
        self.repo = repo

    def getAll(self):
        return self.repo.getAll()

    def isDuplicate(self, ccode):
        return self.repo.search(ccode) != None
    
    def addFirst(self, booking):
        self.repo.addFirst(booking)

    def addLast(self, booking):
        self.repo.addLast(booking)
    
    def isExist(self, bcode, ccode):
        for booking in self.getAll():
            if booking.bcode == bcode and booking.ccode == ccode:
                return True
        return False
    
    def sort(self):
        if self.repo.isEmpty():
            return self.repo

        nodes = []
        for booking in self.getAll():
            nodes.append(booking)

        for i in range(1, len(nodes)):
            current_node = nodes[i]
            j = i - 1
            while j >= 0 and (nodes[j].bcode > current_node.bcode or (nodes[j].bcode == current_node.bcode and nodes[j].ccode > current_node.ccode)):
                nodes[j + 1] = nodes[j]
                j -= 1
            nodes[j + 1] = current_node

        self.repo.clear()
        for node in nodes:
            self.addLast(node)

        return self.getAll()
            