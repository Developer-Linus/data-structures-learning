import array


class FixedArray:
    def __init__(self, type_code, size):
        self.type_code = type_code
        self.size = size
        self.arr = array.array(self.type_code)
        self.length = 0

    def insert(self, value):
        if self.length < self.size:
            self.arr.append(value)
            print(f"{value} added to the array.")
            self.length += 1
        else:
            print("Array is full.")

    def delete(self, value):
        if value in self.arr:
            self.arr.remove(value)
            print(f"{value} deleted from the array.")
            self.length -= 1
        else:
            print(f"{value} not in the array.")

    def find(self, target):
        for index in range(self.length):
            if self.arr[index] == target:
                return (index, target)
        return None

    def search(self, target):
        indices = []
        for index in range(self.length):
            if self.arr[index] == target:
                indices.append(index)
        if indices:
            return (target, indices)
        return None

    def traverse(self, callback):
        for index in range(self.length):
            callback(self.arr[index])

    def display(self):
        print(list(self.arr))


a = FixedArray("i", 6)
a.insert(3)
a.insert(5)
a.insert(4)
a.insert(5)
a.insert(5)
a.insert(5)

print(a.search(5))
print(a.find(12))
a.traverse(print)


a.delete(12)
a.delete(5)
a.display()
