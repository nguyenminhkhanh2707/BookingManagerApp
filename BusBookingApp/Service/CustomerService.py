import csv
import os
from Model.Customer import Customer

class CustomerService:
    def __init__(self, repo):
        self.repo = repo

    def convert_row_to_object(self, row):
        return Customer(row['ccode'], row['name'], (row['phone']))
    
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
                writer.writerow(['ccode', 'name', 'phone'])
      
                for customer in self.getAll():
                    writer.writerow([customer.ccode, customer.name, customer.phone])

            print(f"Saved to {filename} successfully.")
        except IOError as e:
            print(f"Error saving file: {e}")

    def getAll(self):
        return self.repo.getAll()

    def isDuplicate(self, ccode):
        return self.repo.search(ccode) != None
    
    def addFirst(self, customer):
        self.repo.addFirst(customer)

    def addLast(self, customer):
        self.repo.addLast(customer)

    def search(self, xCode):
        return self.repo.search(xCode)
    
    def dele(self, xCode):
        customer = self.search(xCode)
        if customer != None:
            self.repo.delete(customer)
            return True
        else:
            return False
