"""
Queue ADT using Doubly Linked List

"""
from DoublyLinkedList import DLinkedList


class NodeQueue:
    def __init__(self):
        self.list = DLinkedList()

    def enqueue(self,data):
        """
        insert value to the end of the queue.

        """
        self.list.append(data)

    def dequeue(self):
        """
        Delete and return the first value from 
        the queue.

        """
        if len(self.list) == 0:
            raise ValueError("Queue is empty !")

        return self.list.popleft()

    def first(self):
        """
        Return the first value from the queue.

        """
        if len(self.list) == 0:
            raise ValueError("Queue is empty !")
        return self.list.get(0)

    def is_empty(self):
        """
        If queue is empty return True else False

        """
        if len(self.list) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self.list)

