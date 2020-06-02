class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            else:
                current = current.next
        return None
    
    def delete(self, value):
        current = self.head

        if current.value == value:
            self.head = self.head.next
            return current
        
        prev = current
        current = current.next

        while current is not None:
            if current.value == value:
                prev.next = current.next
                return current
            else:
                prev = prev.next
                current = current.next