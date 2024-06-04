class Node:
    def __init__(self, el):
        self.data = el
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def addFirst(self, el):
        new_node = Node(el)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def addLast(self, el):
        new_node = Node(el)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addPos(self, el, pos):
        if pos == 0:
            self.addFirst(el)
            return

        prev = None
        curr = self.head
        for i in range(pos):
            prev = curr
            curr = curr.next

        if curr is None:
            return

        new_node = Node(el)
        new_node.next = curr
        if prev is None:
            self.head = new_node
        else:
            prev.next = new_node

    def addMany(self, arr):
        for el in arr:
            self.addLast(el)

    def size(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def get(self, pos):
        if pos < 0 or pos >= self.size():
            return None

        curr = self.head
        for i in range(pos):
            curr = curr.next
        return curr.data

    def indexOf(self, el):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == el:
                return index
            index += 1
            curr = curr.next
        return -1

    def removeFirst(self):
        if self.isEmpty():
            return None

        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def removeLast(self):
        if self.isEmpty():
            return None

        if self.head == self.tail:
            return self.removeFirst()

        prev = None
        curr = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next

        prev.next = None
        self.tail = prev
        return curr.data

    def removeAll(self, el):
        while self.head is not None and self.head.data == el:
            self.head = self.head.next

        curr = self.head
        prev = None
        while curr is not None:
            if curr.data == el:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        if curr is None:
            self.tail = prev

if __name__ == "__main__":
    sll = SLL()

    # Kiểm tra isEmpty
    print(sll.isEmpty())  # True

    # Thêm phần tử vào đầu danh sách
    sll.addFirst(10)
    sll.addFirst(20)
    sll.addFirst(30)

    # Kiểm tra isEmpty
    print(sll.isEmpty())  # False

    # In danh sách
    curr = sll.head
    while curr is not None:
        print(curr.data)
        curr = curr.next

    # Thêm phần tử vào cuối danh sách
    sll.addLast(40)
    sll.addLast(50)

    # In kích thước danh sách
    print(sll.size())  # 5

    # Lấy phần tử theo vị trí
    print(sll.get(2))  # 30

    # Tìm kiếm vị trí phần
