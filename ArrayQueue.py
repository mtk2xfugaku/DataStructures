"""
Queue using circular array
Queue uses FIFO (i.e. First In First Out) dynamic operations.

"""

class ArrayQueue:
    capacity = 10 
    def __init__(self):
        self.__queue = [None] * ArrayQueue.capacity
        self.__size = 0
        self.__f = 0

    def __resize(self,cap):
        prev = self.__queue
        self.__queue = [None] * cap
        trav = self.__f
        for i in range(self.__size):
            self.__queue[i] = prev[trav]
            trav = (trav + 1) % len(prev)
        self.__f = 0

    def is_empty(self):
        return self.__size == 0 or False

    def __len__(self):
        return self.__size

    def first(self):
        if self.is_empty():
            raise ValueError("Queue is empty !")

        return self.__queue[self.__f]

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty !")
        ret_val = self.__queue[self.__f]
        self.__queue[self.__f] = None
        self.__f = (self.__f + 1) % len(self.__queue)
        self.__size -= 1

        # if the number of elements reduce by a factor of 1/4
        # shrinking the queue by a factor of 1/2

        if 0 < self.__size < len(self.__queue)//4:
            self.__resize(len(self.__queue) // 2)
        return ret_val

    def enqueue(self,data):
        if self.__size == len(self.__queue):
            self.__resize(2 * len(self.__queue))
        pos = (self.__f + self.__size) % len(self.__queue)
        self.__queue[pos] = data
        self.__size += 1

    def __getitem__(self,index):
        if not 0 <= index < len(self.__queue):
            raise IndexError("Index out of bound !")
        pos = (self.__f + index) % len(self.__queue)
        return self.__queue[pos]

    def __setitem__(self,index,data):
        if not 0 <= index < len(self.__queue):
            raise IndexError("Index out of bound !")
        pos = (self.__f + index ) % len(self.__queue)
        self.__queue[pos] = data
        

