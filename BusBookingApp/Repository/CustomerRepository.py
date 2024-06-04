from Model.MyCircularLinkedList import MyCircularLinkedList

class CustomerRepository:
    def __init__(self):
        self.customer_list = MyCircularLinkedList()
    
    def getAll(self):
        return self.customer_list
    
    def setList(self, linked_list):
        self.customer_list = linked_list

    def addFirst(self, customer):
        self.customer_list.addFirst(customer)

    def addLast(self, customer):
        self.customer_list.addLast(customer)

    def isEmpty(self):
        return self.customer_list.isEmpty()
    
    def delete(self, customer):
        self.customer_list.delete(customer)

    def search(self, xCode):
        for customer in self.getAll():
            if customer.ccode == xCode:
                return customer
        return None
    
    def clear(self):
        self.customer_list.head = None