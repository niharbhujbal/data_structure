class Array:
    """
    An Array Data Structure
    """
    def __init__(self, datatype : str, length: int = 0 ):
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
        if self.datatype == 'int':
            self.items = [0] * self.length
        elif self.datatype == 'str':
            self.items = [''] * self.length

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
        if (index < 0) or (function == 'insert' and index > self.length) or (function == 'remove' and index >= self.length):
            raise IndexError('Index Out of range')


    def insert(self, value, index = None):
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
        if index is None :
            index = self.length

        # validate the index
        self._validate_index(index,'insert')

        if self.datatype == 'int':
            new_items = [0] * (self.length+1)
        elif self.datatype == 'str':
            new_items = [''] * (self.length+1)
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
        self.validate_index(index,'remove')

        # copy all the elements to left side of array
        for inside_index in range(index + 1, self.length):
            self.items[inside_index-1] = self.items[inside_index]

        # delete last elemnet of the array
        del self.items[self.length-1]
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