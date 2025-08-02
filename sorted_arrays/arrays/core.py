import array


class Array:
    """
    Static array implementation with fixed capacity
    and specific type of data
    """

    def __init__(self, max_size, typecode="i"):
        self._data = array.array(typecode, [0]*max_size)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def max_size(self):
        return len(self._data)
