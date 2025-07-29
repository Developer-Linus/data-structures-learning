import array


class FixedUnsortedArray:

    """Sets the maximum array size and creates an empty array.array"""

    def __init__(self, size, type_code):
        self.size = size
        self.type_code = type_code
        self.arr = array.array(self.type_code)
        self.length = 0

    """Inserts new element if there is room"""

    def insert(self, value):
        if self.length < self.size:
            self.arr.append(value)
            self.length += 1
            print(f"Inserted {value}")
        else:
            print("Array is full. Cannot insert more elements.")

    def delete(self, value):
        if value in self.arr:
            self.arr.remove(value)
            self.length -= 1
            print(f"Deleted {value}")
        else:
            print(f"Value {value} not found in the array.")

    def display(self):
        print("Current array elements: ", list(self.arr))


a = FixedUnsortedArray(6, "i")

a.insert(4)
a.insert(12)
a.insert(14)
a.insert(16)
a.insert(20)
a.insert(65)

a.display()
a.insert(22)
a.delete(12)
a.display()
a.delete(344)
