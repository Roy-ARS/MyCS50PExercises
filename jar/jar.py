class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("That many cookies does not fit into the jar")
        self.size += n

    def withdraw(self, n):
        if (self.size - n) < 0:
            raise ValueError("Jar does not have that many cookies")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            int(capacity)
        except:
            raise ValueError("Not an integer number")

        if 0 > capacity:
            raise ValueError("Not a positive number")

        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Jar can not contain that many cookies")
        self._size = size
