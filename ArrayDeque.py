"""
TODO : Implement a deque using an Array Deque(Readmore on wikipedia.com/wiki/Double-ended_queue).

Required operations and time complexitites 

1. push(e) 
2. pushleft(e)
3. pop()
4. popleft()

All dynamic operations must have O(1) Amortized time 


This is a circular array 
"""

class ArrayDeque:
    max_capacity = 10

    def __init__(self):
        self.__deque = [None] * ArrayDeque.max_capacity
        self.__f = 0
        self.__size = 0
    
    def __resize(self,new_cap):
        temp = self.__deque
        self.__deque = [None] * new_cap
        trav = self.__f
        for i in range(self.__size):
            self.__deque[i] = temp[trav]
            trav = (trav + 1) % len(temp)
        
        self.__f = 0
    
    def is_empty(self):
        """
        Return True if Deque is empty 

        """
        return self.__size == 0
    
    def clear(self):
        if self.is_empty():
            raise ValueError
        self.__deque = [None] * ArrayDeque.max_capacity
        self.__size = 0

    def appendleft(self,data):
        if self.__size == len(self.__deque):
            self.__resize(2 * len(self.__deque))
        
        # find the first index position in a circular array.

        pos = (self.__f - 1) % len(self.__deque)
        
        self.__deque[pos] = data
        
        self.__f = pos
        
        self.__size += 1
    
    def popleft(self):
        if self.is_empty():
            raise ValueError
        
        ret_val = self.__deque[self.__f]
        self.__deque[self.__f] = None
        self.__f = (self.__f + 1) % len(self.__deque)
        self.__size -= 1

        if 0 < self.__size < len(self.__deque)//4:
            self.__resize(len(self.__deque) // 2)
        return ret_val
    
    def append(self,data):
        if self.__size == len(self.__deque):
            self.__resize(2 * len(self.__deque))
        
        pos = (self.__f + (self.__size)) % len(self.__deque)
        self.__deque[pos] = data
        self.__size += 1
    
    def pop(self):
        if self.is_empty():
            raise ValueError
        
        pos = (self.__f + (self.__size - 1)) % len(self.__deque)
        ret_val = self.__deque[pos]
        self.__deque[pos] = None
        self.__size -= 1
        
        if 0 < self.__size < len(self.__deque)//4:
            self.__resize(len(self.__deque) // 2)
        
        return ret_val
    
    def peek(self):
        if self.is_empty():
            raise ValueError
        pos = (self.__f + (self.__size - 1)) % len(self.__deque)
        return self.__deque[pos]
    
    def peekleft(self):
        if self.is_empty():
            raise ValueError
        return self.__deque[self.__f]
    
    def __len__(self):
        return self.__size
    
    def __getitem__(self,index):
        # random access in O(1) time.
        if not 0 <= index < len(self.__deque):
            raise IndexError("Index out of bound !")
        pos = (self.__f + index) % len(self.__deque)
        return self.__deque[pos]
    
    
    def __iter__(self):
        if self.__size == 0:
            raise ValueError
        f = self.__f
        for i in range(self.__size):
            yield self.__deque[f]
            f = (f + 1) % len(self.__deque)
        
    def actualSize(self):
        # this is just for testing because self.__deque is private data field.
        return self.__deque






