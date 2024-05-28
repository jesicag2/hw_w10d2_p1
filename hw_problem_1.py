# HW_P1: Implementing a Singly Linked List in Python
'''
Objective: The aim of this assignment is to reinforce understanding of the singly linked list data structure and its implementation in Python.

Problem Statement: You are tasked with implementing a singly linked list class in Python. The class should support basic operations such as insertion, deletion, and traversal.
'''
# Task 1
# Implement the Node class to represent individual nodes in the linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


# Task 2
# Implement the SinglyLinkedList class with methods for insertion, deletion, and traversal.
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)

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

    def traverse(self): 
        print('Linked List Elements:')
        print('head\n | \n V')
        current = self.head

        while current:
            print(current, end=' -> ')
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
            prev_node.next = new_node

    def remove(self, value_to_remove):
        if self.head is None:
            print('List is empty, nothing to remove')
            return

        if self.head.value == value_to_remove:
            self.head = self.head.next
            return

        current_node = self.head

        while current_node.next:
            if current_node.next.value == value_to_remove:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next
        print(f"{value_to_remove} is not in this Linked List.")


# Task 3
# Test the implemented functionality by performing various operations on the linked list.
strawhats = SinglyLinkedList()
strawhats.append('Nami')
strawhats.append('Sanji')
strawhats.push('Zoro')
strawhats.push('Luffy')
strawhats.append('Chopper')
strawhats.append('Franky')
strawhats.insert_after('Nami', 'Usopp')
strawhats.insert_after('Chopper', 'Robin')
strawhats.append('Brook')
strawhats.append('Jinbe')
strawhats.traverse()
