class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None

    def is_empty(self):
        return self.headval is None

    def display(self):
        current_node = self.headval
        while current_node:
            print(current_node.dataval, end=" ")
            current_node = current_node.nextval
        print()

    def update_value_at_position(self, position, new_data):
        if self.is_empty():
            print("Linked list is empty. Cannot update value.")
            return

        current_node = self.headval
        current_position = 0

        while current_node:
            if current_position == position:
                current_node.dataval = new_data
                return
            current_node = current_node.nextval
            current_position += 1

        print(f"Position {position} not found in the linked list. Cannot update value.")

    def insert_in_middle(self, middle_node, new_data):
        if middle_node is None:
            print("The given middle node must be a valid node in the linked list.")
            return

        new_node = Node(new_data)
        new_node.nextval = middle_node.nextval
        middle_node.nextval = new_node

        # Update the tailval if the new node is inserted at the end
        if new_node.nextval is None:
            self.tailval = new_node


class Stack:
    def __init__(self, linked_list=None):
        self.linked_list = linked_list if linked_list else LinkedList()

    def is_empty(self):
        return self.linked_list.is_empty()

    def push(self, dataval):
        new_node = Node(dataval)
        new_node.nextval = self.linked_list.headval
        self.linked_list.headval = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None

        popped_value = self.linked_list.headval.dataval
        self.linked_list.headval = self.linked_list.headval.nextval
        return popped_value

    def update_value_at_position(self, position, new_data):
        self.linked_list.update_value_at_position(position, new_data)

    def display(self):
        print("Stack:")
        self.linked_list.display()


class Queue:
    def __init__(self, linked_list=None):
        self.linked_list = linked_list if linked_list else LinkedList()

    def is_empty(self):
        return self.linked_list.is_empty()

    def enqueue(self, dataval):
        new_node = Node(dataval)
        if self.is_empty():
            self.linked_list.headval = new_node
            self.linked_list.tailval = new_node
        else:
            self.linked_list.tailval.nextval = new_node
            self.linked_list.tailval = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        dequeued_value = self.linked_list.headval.dataval
        self.linked_list.headval = self.linked_list.headval.nextval
        return dequeued_value

    def update_value_at_position(self, position, new_data):
        self.linked_list.update_value_at_position(position, new_data)

    def display(self):
        print("Queue:")
        self.linked_list.display()


if __name__ == '__main__':
    linked_list = LinkedList()

    # Menambahkan beberapa node
    linked_list.headval = Node(1)
    second_node = Node(2)
    third_node = Node(4)
    fourth_node = Node(6)
    fifth_node = Node(9)

    linked_list.headval.nextval = second_node
    second_node.nextval = third_node
    third_node.nextval = fourth_node

    linked_list.tailval = fifth_node  # Update tailval

    print("Linked List sebelum penambahan di tengah:")
    linked_list.display()

    # Menambahkan node di tengah
    middle_node = second_node
    new_data = 90
    linked_list.insert_in_middle(middle_node, new_data)

    stack = Stack(linked_list)
    stack.push(10)

    stack.update_value_at_position(1, 4)

    print("\nLinked List setelah penambahan di tengah:")
    linked_list.display()
