class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyCircularLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
            if current == self.head:
                break

    def isEmpty(self):
        return self.head is None
    
    def addLast(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def addFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def addBefore(self, position, data):
        if position == 0:
            self.addFirst(data)

        new_node = Node(data)
        count = 0
        current = self.head
        prev = None
        while current:
            if count == position:
                prev.next = new_node
                new_node.next = current
                return
            prev = current
            current = current.next
            count += 1

    def delete(self, key):
        if self.head is None:
            return

        # If the head is the node to be removed
        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return

        # Search for the node to be removed
        prev = None
        current = self.head
        while current.next != self.head:
            if current.data == key:
                break
            prev = current
            current = current.next

        # If the node with key is found, remove it
        if current.data == key:
            prev.next = current.next
        else:
            print("Node not found")

    def update(self, old_data, new_data):
        if self.head is None:
            return False

        current = self.head
        while True:
            if current.data == old_data:
                current.data = new_data
                return True
            current = current.next
            if current == self.head:
                break
            
        return False