# HW_P2: Implementing a Doubly Linked List in Python
'''
Objective: The aim of this assignment is to introduce students to the doubly linked list data structure and its implementation in Python.

Problem Statement: You are tasked with implementing a doubly linked list class in Python. The class should support operations such as insertion, deletion, and traversal.
'''

# Task 1
# Implement the **Node** class to represent individual nodes in the doubly linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


# Task 2
# Implement the **DoublyLinkedList** class with methods for insertion, deletion, and traversal.
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)

        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def append(self, new_value): 
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def traverse(self): 
        print('Linked List Elements:')
        print('head\n | \n V')
        current = self.head
        while current:
            print(current, end=' <--> ')
            current = current.next
        print(None)

    def get_node(self, value_to_get): 
        node_to_check = self.head
        while node_to_check:
            if node_to_check.value == value_to_get:
                return node_to_check
            node_to_check = node_to_check.next
        return None

    def insert_after(self, prev_value, new_value): 
        prev_node = self.get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in the linked list")
        else:
            new_node = Node(new_value)
            new_node.next = prev_node.next
            if prev_node.next:
                prev_node.next.prev = new_node
            prev_node.next = new_node
            new_node.prev = prev_node

    def remove(self, value_to_remove):
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        if self.head.value == value_to_remove:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.value == value_to_remove:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
        print(f"{value_to_remove} is not in this Linked List.")


# Task 3
# Test the implemented functionality by performing various operations on the doubly linked list.
days = DoublyLinkedList()
days.push('Monday')
days.append('Thursday')
days.append('Saturday')
days.push('Sunday')
days.insert_after('Monday', 'Tuesday')
days.insert_after('Tuesday', 'Wednesday')
days.insert_after('Thursday', 'Friday')

days.traverse()