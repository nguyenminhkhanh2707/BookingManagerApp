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
