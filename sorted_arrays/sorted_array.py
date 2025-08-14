from arrays.core import Array


class SortedArray:
    """
    A class that manages fixed-size static array
    Ensures elements are in ascending order and prevent external mutation
    """

    def __init__(self, max_size, typecode="i"):
        """
        Initializes a new sorted array with a fixed capacity

        Args: 
            max_size(int): maximum number of arrays an element can hold.
            typecode(str): type of elements, default is 'i' (signed integers)
        """
        self._array = Array(max_size, typecode)
        self._max_size = max_size
        # Tracks how many elements are actually inserted (used length)
        self._size = 0

    def __len__(self):
        """
        Returns the number of elements stored in a sorted array.
        Returns:
            int: number of elements currently stored
        """
        return self._size

    def insert(self, value):
        """
        Inserts a value into a sorted array while maintaining order

        The algorithm works by shifting elements to the right
        until the position of the new value is found. This maintains the invariant
        that the array is always sorted in ascending order. 

        Args:
            value (int or float): the value to insert.

        Raises:
            ValueError: if the array is already full.
        """
        if self._size >= self._max_size:
            raise ValueError(
                f"The array is already full, maximum size, {self._max_size}")
        # Start from the end and shift the elements until we find the insertion point
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                # Shift the larger value to the right
                self._array[i] = self._array[i-1]
        # If we get here, the value is the smallest and should be inserted at index 0
        self._array[0] = value
        self._size += 1

    def traverse(self):
        """
        Returns the elements of the sorted array as python list
        Returns:
            List (int or float): all inserted elements in sorted order
        """
        return [self._array[i] for i in range(self._size)]

    def __str__(self):
        """
        Return string representation of the array's current sorted contents.
        """
        return str(self.traverse())

    def linear_search(self, target):
        """
        Searches for target from left to right of the array (linear search)
        """
        for i in range(self._size):
            if self._array[i] == target:
                return i
            # For sorted array, if the current element is larger than target, then there is no need to continue searching
            elif self._array[i] > target:
                return None
        return None

    def binary_search(self, target):
        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left+right)//2
            mid_value = self._array[mid_index]
            if mid_value == target:
                return mid_index
            elif mid_value > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return None

    def delete(self, target):
        index = self.binary_search(target)
        if index is None:
            return ValueError(f'Unable to delete element {target}: the entry is not in the array')
        for i in range(index, self._size-1):
            self._array[i] = self._array[i+1]


a = SortedArray(7, "i")
print(a.traverse())
a.insert(12)
a.insert(2)
a.insert(1)
a.insert(20)
a.insert(45)
print(a.traverse())
print(a.linear_search(2))
a.delete(20)
print(a.traverse())
