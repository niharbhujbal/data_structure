class Array:
    """
    An Array Data Structure
    """

    def __init__(self, datatype: str, length: int = 0):
        """
        Intitalisation of Array Structure
        -------------
        Parameters
        -------------
        datatype : str
            the datatype of the array elements
        length : int
            length of the array you want to define. if not defined it will be 0
        """
        self.length = length
        self.datatype = datatype
        if self.datatype == "int":
            self.items = [0] * self.length
        elif self.datatype == "str":
            self.items = [""] * self.length

    def print_items(self):
        """
        Print all the Items in Array
        """
        for item in self.items:
            print(item)

    def __len__(self):
        """
        length of array
        """
        return self.length

    def _validate_index(self, index: int, function: str):
        """
        validate if the index is in range for the array
        -------------
        Parameters
        -------------
        index : int
        index we want to check
        function : str
        for which function you want to use this validation
        values can be 'insert' or 'remove'
        """
        if (
            (index < 0)
            or (function == "insert" and index > self.length)
            or (function == "remove" and index >= self.length)
        ):
            raise IndexError("Index Out of range")

    def insert(self, value, index=None):
        """
        Insert a value at the end of array if no index is given.
        with a index it will add the value in that location of the array
        -------------
        Parameters
        -------------
        value : int / str
        value you want to be inserted
        index : int
        index at which you want to insert the value. by default it will insert item at the end
        """
        # defining default value of Index
        if index is None:
            index = self.length

        # validate the index
        self._validate_index(index, "insert")

        if self.datatype == "int":
            new_items = [0] * (self.length + 1)
        elif self.datatype == "str":
            new_items = [""] * (self.length + 1)
        new_index = 0

        # if the value we want to insert is between the array
        for item in self.items:
            if new_index == index:
                new_items[new_index] = value
                new_index += 1

            new_items[new_index] = item
            new_index += 1

        # if we want to insert the value at the end
        if index == self.length:
            new_items[index] = value

        # Copying new array in instance and updating new length
        self.items = new_items
        self.length += 1

    def removeAt(self, index: int):
        """
        Remove value from array at specific index
        -------------
        Parameters
        -------------
        index : int
        index from which you want to remove the value
        """
        # validate the index
        self.validate_index(index, "remove")

        # copy all the elements to left side of array
        for inside_index in range(index + 1, self.length):
            self.items[inside_index - 1] = self.items[inside_index]

        # delete last elemnet of the array
        del self.items[self.length - 1]
        self.length -= 1

    def indexOf(self, value: int) -> int:
        """
        Return the index of value passed from array or -1 if value is not present in the array
        -------------
        Parameters
        -------------
        value : int
        value of which we want to find the index
        ------------
        Return
        ------------
        index : int
        index of the value in array
        """
        index = 0
        # check the index of the value
        for item in self.items:
            if item == value:
                return index
            index += 1
        # if value was matched then return -1
        else:
            return -1


class LinkedList:
    """
    A LinkedList Data Structure
    """

    def __init__(self):
        """
        Intitalisation of LinkedList Structure
        """
        self.first_node = self.Node()
        self.last_node = self.Node()
        self.list_size = 0

    class Node:
        """
        Node object which contains value and address of next object
        """

        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def addLast(self, value):
        """
        Add a value in the last of linked list
        ----------
        Parameter
        ----------
        value : int / str
        value you want to add in the list
        """
        node = self.Node(value)
        # if the list is empty
        if self.first_node.value is None:
            self.first_node = node
            self.last_node = node
        # if array has more than zero elements
        else:
            self.last_node.next = node
            self.last_node = node
        # incrementing the size of list
        self.list_size += 1

    def addFirst(self, value):
        """
        Add a value at the first of linked list
        ----------
        Parameter
        ----------
        value : int / str
        value you want to add in the list
        """
        node = self.Node(value)
        # if the list is empty
        if self.first_node.value is None:
            self.first_node = node
            self.last_node = node
        # if array has more than zero elements
        else:
            node.next = self.first_node
            self.first_node = node
        # incrementing the size of list
        self.list_size += 1

    def indexOf(self, value) -> int:
        """
        Find out the index of the input value in the list
        return -1 if value not present in the list
        ----------
        Parameter
        ----------
        value : int / str
        value for which you want to find index for
        """
        index = 0
        current = self.first_node
        while current is not None:
            if current.value == value:
                return index
            else:
                current = current.next
            index += 1
        # if value is not in the list
        return -1

    def contains(self, value):
        """
        checck whether the value is present in the list
        ----------
        Parameter
        ----------
        value : int / str
        the value
        """
        return self.indexOf(value) != -1

    def removeFirst(self):
        """
        remove first element from the list
        """
        # if list is empty
        if self.first_node.value is None:
            raise Exception("No such element Found")
        # if list only has one value
        elif self.first_node == self.last_node:
            self.first_node, self.last_node = None, None
        # if list has more than one value
        else:
            self.first_node, self.first_node.next = self.first_node.next, None
        self.list_size -= 1

    def removeLast(self):
        """
        remove last element from the list
        """
        # if list is empty
        if self.first_node.value is None:
            raise Exception("No such element Found")

        current = self.first_node
        while current != None:
            if current.next == self.last_node:
                break
            current = current.next

        # if list only has one value
        if self.first_node == self.last_node:
            self.first_node, self.last_node = None, None
        else:
            current.next, self.last_node = None, current
        self.list_size -= 1

    def size(self):
        """
        find out the size of list
        """
        return self.list_size

    def toArray(self):
        """
        convert the LinkedList to Array
        """
        converted_array = Array("int")
        current = self.first_node
        while current != None:
            converted_array.insert(current.value)
            current = current.next
        return converted_array

    def reverse(self):
        """
        we reverse the linkedlist
        """
        # if there is no items in list then we just return none
        if self.first_node.value is None:
            return None

        # we reverse the links in the list
        previous = self.first_node
        current = self.first_node.next
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next

        # change the first and last head and clear the next reference in last pointer
        self.last_node = self.first_node
        self.last_node.next = None
        self.first_node = previous

    def Kth_node_from_last(self, k):
        # handeling cases when k is less than equal
        if k > self.list_size and k > 0:
            raise Exception(
                "Invalid K argument. It should be grater than 0 and less than size of list"
            )
        if k == self.list_size:
            return self.first_node

        a = self.first_node
        b = self.first_node
        for i in range(k - 1):
            b = b.next
        while b != self.last_node:
            a = a.next
            b = b.next
        return a


class Stack:
    """
    A Stack Data Structure using Array
    """

    def __init__(self, datatype: str, height: int):
        """
        Intitalisation of Stack Structure
        -------------
        Parameters
        -------------
        datatype : str
          the datatype of the stack
        height : int
          height of the array
        """
        self.stack_data = Array(datatype, height)
        self.height = 0

    def print_items(self):
        """
        Print all the items in Stack bottom up
        """
        counter = 0
        for item in self.stack_data:
            if counter < self.height:
                print(item)
            counter += 1

    def push(self, value):
        """
        Push an item into stack
        -------------
        Parameters
        -------------
        value : str / int
          item you want to push in stack
        """
        # if the stack is full
        if (self.height + 1) > self.stack_data.length:
            raise Exception("Stack Over Flow Error")
        # otherwise just incert the value
        else:
            self.stack_data.insert(value, self.height)
            self.height += 1
            self.stack_data.removeAt(self.height)

    def pop(self):
        """
        Get the top item on the stack and remove it from stack
        """
        # if stack is empty
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            item = self.stack_data.items[self.height - 1]
            if self.stack_data.datatype == "int":
                self.stack_data.insert(0, self.height - 1)
            elif self.stack_data.datatype == "str":
                self.stack_data.insert("0", self.height - 1)
            self.stack_data.removeAt(self.height)
            self.height -= 1
            return item

    def peek(self):
        """
        look at the top item of stack. this does not remove the item from stack
        """
        if self.height - 1 < 0:
            return None
        else:
            return self.stack_data.items[self.height - 1]

    def isEmpty(self) -> bool:
        """
        Returns whether the stack is empty
        """
        return self.height == 0


class Queues:
    """
    An Queue Data Structure
    """

    def __init__(self, datatype: str, length: int):
        """
        Intitalisation of Queue Structure
        -------------
        Parameters
        -------------
        datatype : str
          the datatype of the queue
        length : int
          length of queue
        """
        self.queue_data = Array(datatype, length)
        self.rear = 0

    def enqueue(self, value):
        """
        add the value at the end of the queue
        -------------
        Parameters
        -------------
        value : int / str
          value we want to add
        """
        if self.isFull():
            raise Exception("Queue is Full")
        else:
            self.queue_data.insert(value, self.rear)
            self.rear += 1
            self.queue_data.removeAt(self.rear)

    def dequeue(self):
        """
        get the first value in the queue and delete it from queue
        """
        if self.isEmpty():
            raise Exception("Queue is Empty")
        else:
            item = self.queue_data.items[0]
            self.queue_data.removeAt(0)
            self.queue_data.insert(0)
            self.rear -= 1
            return item

    def peek(self):
        """
        Look at the first value in queue. it does not delete the value from queue
        """
        if self.rear == 0:
            return None
        else:
            return self.queue_data.items[0]

    def isEmpty(self) -> bool:
        """
        Boolen vaue whether the queue is empty
        """
        return self.rear == 0

    def isFull(self) -> bool:
        """
        Boolen value whether the queue is full
        """
        return self.rear == self.queue_data.length


class PriorityQueue(Queues):
    """
    a Priority Queue Data Structure
    """

    def __init__(self, datatype: str, length: int):
        """
        Intitalisation of Queue Structure
        """
        super().__init__(datatype, length)

    def add(self, value):
        """
        adds the value based on the items in the queue such that queue is kept in ascending order
        -------------
        Parameters
        -------------
        value : int / str
          value we want to add
        """
        if self.isFull():
            raise Exception("Queue is Full")
        elif self.isEmpty():
            self.enqueue(value)
        else:
            for index_ in range(self.rear):
                if value <= self.queue_data.items[index_]:
                    self.queue_data.insert(value, index_)
                    self.queue_data.removeAt(self.rear + 1)
                    self.rear += 1
                    break
            else:
                self.enqueue(value)
