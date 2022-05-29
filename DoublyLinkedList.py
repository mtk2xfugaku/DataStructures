"""
Doubly linked list 

insert_at() and delete_at() doesn't require resizing the whole structure. 

so insertion/deletion at an arbitrary location requires O(k) + O(1) time 

O(k) for traversing the structure since random access is not possible in a linked structure.
O(1) because no resizing is needed for mutation.

"""


class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    # wrapper class to manipulate nodes.
    def __init__(self):
        self.headnode = node() # headnode contains no data only next reference.
        self.tailnode = None   # tailnode contains data
        self.nodecount = 0     # nodecount contains number of data elements in node
    
    def isEmpty(self):
        return self.nodecount == 0

    def append(self,data):
        """
        Insert a new node at the end of the 
        linked list.

        """
        new_node = node(data)
        if self.headnode.next == None:
            self.headnode.next = new_node
            new_node.prev = self.headnode
            self.tailnode = new_node
        else:
            temp = self.tailnode
            temp.next = new_node
            new_node.prev = temp
            self.tailnode = new_node

        self.nodecount += 1

    def appendleft(self,data):
        """
        Insert a new node at the start of 
        the linked list.

        """
        if self.isEmpty():
            raise ValueError("Linked List Empty !")
        new_node = node(data)
        temp = self.headnode.next
        self.headnode.next = new_node
        new_node.prev = self.headnode
        new_node.next = temp
        temp.prev = new_node
        self.nodecount += 1

    def pop(self):
        """
        Delete and return the last 
        node's data

        """
        if self.nodecount == 0:
            raise ValueError("List is Empty !")

        value = self.tailnode.data
        keep = self.tailnode.prev
        keep.next = None
        self.tailnode = keep
        self.nodecount -= 1
        return value


    def popleft(self):
        """
        Delete and return the first 
        node's data
        """
        if self.headnode.next == None:
            raise ValueError
        if self.nodecount == 1:
            temp = self.headnode.next
            ret_val = temp.data
            temp = temp.next
            self.headnode.next = temp
            self.nodecount -= 1
            return ret_val

        temp = self.headnode.next
        ret_val = temp.data
        temp = temp.next
        self.headnode.next = temp
        temp.prev = self.headnode
        self.nodecount -= 1
        return ret_val




    def insert_at(self,index,data):
        """
        Insert at an index position 
        """
        if not 0 <= index < self.nodecount:
            raise IndexError
        new_node = node(data)
        i = 0
        current = self.headnode
        while current.next != None:
            if i == index:
                temp = current.next
                current.next = new_node
                new_node.prev = current
                new_node.next = temp
                temp.prev = new_node
            current = current.next
            i += 1
        
        self.nodecount += 1



    def delete_at(self,index):
        """
        Delete at an index position
        """
        if not 0 <= index < self.nodecount:
            raise IndexError
        i = 0
        current = self.headnode
        value = 0
        while current.next != None:
            if i == index:
                temp = current.next
                value = temp.data
                current.next = temp.next
                temp = current.next
                temp.prev = current
            current = current.next
            i += 1

        self.nodecount -= 1
        return value

    def peekleft(self):
        if self.nodecount == 0:
            raise ValueError
        temp = self.headnode.next
        return temp.data

    def peek(self):
        if self.nodecount == 0:
            raise ValueError
        # tail node is not the sential node 
        # just the refence to the last node
        return self.tailnode.data

    def get(self,index):
        """
        Return an item at a perticular
        index position.

        """
        if not 0 <= index < self.nodecount:
            raise IndexError
        current = self.headnode
        i = 0
        while current.next != None:
            current = current.next
            if index == i:
                return current.data
            i += 1

    # magic methods 
    def __len__(self):
        return self.nodecount

    def __getitem__(self,index):
        if  not 0 <= index < self.nodecount:
            raise IndexError
        current = self.headnode
        i = 0
        while current.next != None:
            current = current.next
            if i == index:
                return current.data
            i += 1
            
    def __setitem__(self,index,data):
        if not 0 <= index < self.nodecount:
            raise IndexError("Index out of bound !")
        current = self.headnode
        i = 0 
        while current.next != None:
            current = current.next
            if index == i:
                current.data = data
            i += 1
    
    def __iter__(self):
        # working with foreach loop.
        # this is now a generator function.
        if self.nodecount == 0:
            return None
        current = self.headnode
        while current.next != None:
            current = current.next
            yield current.data
        
    def printAll(self):
        """
        Return all the items stored in 
        the linked list.
        """
        vals = []
        current = self.headnode
        while current.next != None:
            current = current.next
            vals.append(current.data)

        return vals

        






