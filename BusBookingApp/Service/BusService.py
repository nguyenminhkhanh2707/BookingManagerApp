import csv
import os
from Model.Bus import Bus

class BusService:
    def __init__(self, repo):
        self.repo = repo

    def convert_row_to_object(self, row):
        return Bus(row['bcode'], row['bus_name'], int(row['seat']), int(row['booked']), float(row['depart_time']), float(row['arrival_time']))
    
    def loadData(self, filename):
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                               
                while not self.repo.isEmpty():
                    user_input = input("The list is not empty. Do you want to keep the existing data? (Y/N): ")
                    if user_input.upper() == "Y": # append
                        for row in reader:
                            self.repo.addLast(self.convert_row_to_object(row))
                        return self.repo.getAll()                                    
                    elif user_input.upper() == "N":
                        self.repo.clear()
                        for row in reader:
                            self.repo.addLast(self.convert_row_to_object(row))  
                        return self.repo.getAll()       
                    else:
                        print("Invalid input. Please enter 'Y' or 'N'.")

                for row in reader:
                    self.repo.addLast(self.convert_row_to_object(row))  
                return self.repo.getAll()       
            
        except IOError as e:
            print(f"Error opening file: {e}")
            return None
        
    def saveAs(self, filename):
        if self.repo.isEmpty():
            print("List is empty. Nothing to save.")
            return

        try:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['bcode', 'bus_name', 'seat', 'booked', 'depart_time', 'arrival_time'])
      
                for bus in self.getAll():
                    writer.writerow([bus.bcode, bus.bus_name, bus.seat, bus.booked, bus.depart_time, bus.arrival_time])

            print(f"Saved to {filename} successfully.")
        except IOError as e:
            print(f"Error saving file: {e}")

    def getAll(self):
        return self.repo.getAll()

    def isDuplicate(self, bcode):
        return self.repo.search(bcode) != None
    
    def addFirst(self, bus):
        self.repo.addFirst(bus)

    def addLast(self, bus):
        self.repo.addLast(bus)

    def addBefore(self, position, bus):
        self.repo.addBefore(position, bus)

    def search(self, xCode):
        return self.repo.search(xCode)
    
    def searchBefore(self, xCode):
        return self.repo.searchBefore(xCode)

    def dele(self, xCode):
        bus = self.search(xCode)
        if bus != None:
            self.repo.delete(bus)
            return True
        else:
            return False
    
    def deleteBefore(self, xCode):
        bus = self.searchBefore(xCode)
        if bus != None:
            self.repo.delete(bus)
            return True
        else:
            return False

    def sortByBcode(self):
        if self.repo.isEmpty():
            return self.repo

        nodes = []
        for bus in self.getAll():
            nodes.append(bus)

        # Sort the list of nodes based on bcode using insertion sort
        for i in range(1, len(nodes)):
            current_node = nodes[i]
            j = i - 1
            while j >= 0 and nodes[j].bcode > current_node.bcode:
                nodes[j + 1] = nodes[j]
                j -= 1
            nodes[j + 1] = current_node

        # Reconstruct the linked list using the sorted nodes
        self.repo.clear()
        for node in nodes:
            self.addLast(node)

        return self.getAll()
    
    def update(self, xcode, new):
        old = self.search(xcode)
        if old != None:
            self.repo.update(old, new)
            return True
        else:
            return False