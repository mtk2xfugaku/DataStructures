
"""
Double Ended Queue using Doubly Linked List

"""

import DoublyLinkedList as d


class NodeDeque:
    def __init__(self):
        # initializing a doubly linked list.
        self.__deque = d.DLinkedList()
    

    def appendleft(self,data):
        """
        Insert element at the left end of the deque.
        O(1)
        """
        self.__deque.appendleft(data)

    def append(self,data):
        """
        Insert element at the right end of the deque.
        O(1)
        """
        self.__deque.append(data)

    def popleft(self):
        """
        Delete and return the left end element of the deque.
        O(1)
        """
        if len(self.__deque) == 0:
            raise ValueError("Deque is empty !")
        return self.__deque.popleft()

    def pop(self):
        """
        delete and return the right end element of the deque.
        O(1)
        """
        if len(self.__deque) == 0:
            raise ValueError("Deque is empty !")
        return self.__deque.pop()

    def peek(self):
        if len(self.__deque) == 0:
            raise ValueError("Deque is empty !")

        return self.__deque.tailnode.data

    def peekFirst(self):
        if len(self.__deque) == 0:
            raise ValueError
        temp = self.__deque.headnode.next
        return temp.data

    def is_empty(self):
        return len(self.__deque) == 0 

    def __len__(self):

        return len(self.__deque)













