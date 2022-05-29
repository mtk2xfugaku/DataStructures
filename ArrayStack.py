"""
Dynamic array based stack implementation 

Follows LIFO (Last in First out)

"""

class ArrayStack:
    def __init__(self):
        self.__array = []

    def push(self,data):
        """
        Insert top of the stack

        """
        self.__array.append(data)
        
    def pop(self):
        """
        return and delete the most 
        recentetly added element of 
        the stack, i.e. top elelment.
        """
        if len(self.__array) == 0:
            raise ValueError("Stack is empty !")
        
        return self.__array.pop()

    def top(self):
        """
        return the recently added 
        element from the stack 

        """
        if len(self.__array) == 0:
            raise ValueError("Stack is empty !")
        return self.__array[-1]

    def is_empty(self):
        if len(self.__array) == 0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.__array)

    def __iter__(self):
        return iter(self.__array)

    def __getitem__(self,index):
        if not 0 <= index < len(self.__array):
            raise IndexError("Index out of bound !")
        return self.__array[index]

    def __setitem__(self,index,data):
        if not 0 <= index < len(self.__array):
            raise IndexError("Index out of bound !")

        self.__array[index] = data





