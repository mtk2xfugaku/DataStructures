

class DynamicArray:
    def __init__(self):
    
        self.size = 0     # number of elements in an array
        self.capacity = 1 # size < capacity always
        self.array = [0]  # Python list used as a static array
    
    # Python magic methods to interface with builtin functions.

    def __len__(self):
        """
        Works with the len() function
        """
        return self.size

    def __iter__(self):
        """
        Works with the ForEach loop 
        Only returns the size not the
        capacity.
        """
        return iter(self.array[:self.size])
    
    def __getitem__(self,key):
        """
        Using subscript to access an index position.

        """
        if key > self.size-1 or key < 0:
            return IndexError("index out of bound !")
        return self.array[key]
    
    def __setitem__(self,key,value):
        """
        Using subscript to set index value to 
        a new value.
        """
        if key > self.size-1 or key < 0:
            return IndexError("index out of bound !")
        self.array[key] = value

    def __contains__(self,item):
        """
        Magic method to work with membership 
        operator.

        """
        if item in self.array:
            return True
        else:
            return False
    
    def __reversed__(self):
        """
        Work with reversed function
        """
        return reversed(self.array)

    # user-defined methods 
    def _resize(self,new_capacity):
        """
        Every time self.size == self.capacity
        resize the array

        """
        empty = [0 for _ in range(new_capacity)]

        # copy the values
        
        for i in range(self.size):
            empty[i] = self.array[i]
        # copy back
        
        self.array = empty
    
        # update the capacity
        self.capacity = new_capacity
    
    def append(self,value):
        """
        Add new values to the last of the array.

        """
        if self.size == self.capacity:
            # increase the capacity by a factor of 2
            self._resize(2 * self.capacity)
        
        # append value at the end
        self.array[self.size] = value
        # update the size
        self.size += 1
    
    def insert_at(self,key,value):
        """
        Insert a new value to a perticular position
        in the array

        """
        # check for space
        if key > self.size-1 or key < 0:
            return IndexError("index out of bound !")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        # shift all values after index key by 1 
        for i in range(self.size-1,key-1,-1):
            self.array[i+1] = self.array[i]
        # insert value at index key
        self.array[key] = value
        # update the size
        self.size += 1
    
    def delete_at(self,key):
        """
        Delete a value in a perticular position
        in the array
        """
        if key > self.size-1 or key < 0:
             return IndexError("index out of bound !")
        for i in range(key,self.size-1):
            self.array[i] = self.array[i+1]
        self.array[self.size-1] = 0
        self.size -= 1

