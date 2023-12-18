class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Node sebelumnya tidak ditemukan.")
            return

        new_node = Node(data)
        new_node.prev = prev_node
        new_node.next = prev_node.next

        if prev_node.next:
            prev_node.next.prev = new_node
        else:
            self.tail = new_node

        prev_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev


# Contoh penggunaan
dll = DoubleLinkedList()
dll.append(1)
dll.append(2)
dll.append(4)

print("Double Linked List sebelum penambahan:")
dll.print_list()

# Menambahkan node 3 setelah node 2
dll.insert_after(dll.head.next, 3)

print("Double Linked List setelah penambahan:")
dll.print_list()
dll.print_reverse()
