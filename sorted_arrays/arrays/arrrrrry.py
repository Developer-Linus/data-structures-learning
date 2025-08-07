from array import array


class Array:
    def __init__(self, typecode, max_size):
        self._data = array(typecode, [0]*max_size)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def max_size(self):
        return len(self._data)
