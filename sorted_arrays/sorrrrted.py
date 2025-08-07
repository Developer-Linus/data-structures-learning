from arrays.arrrrrry import Array


class SortedArray:
    def __init__(self, typecode, max_size):
        self._array = Array(typecode, max_size)
        self._max_size = max_size
        self._size = 0

    def __len__(self):
        return self._size

    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError("The array is already full")
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= value:
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i-1]
        self._array[0] = value
        self._size += 1

    def traverse(self):
        return [self._array[i] for i in range(self._size)]


a = SortedArray("i", 7)
print(a.traverse())
a.insert(34)
a.insert(35)
a.insert(38)
a.insert(40)
a.insert(45)
a.insert(32)

print(a.traverse())
a.__len__()
