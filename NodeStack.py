"""
Stack ATD based on Doubly Linked List 

"""

from DoublyLinkedList import DLinkedList

class NodeStack:
    def __init__(self):
        self.list = DLinkedList()

    def push(self,data):
        self.list.append(data)
    def pop(self):
        if len(self.list) == 0:
            raise ValueError("Stack is empty !")
        return self.list.pop()

    def top(self):
        if len(self.list) == 0:
            raise ValueError("Stack is empty !")
        return self.list.tailnode.data

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.list)
    


