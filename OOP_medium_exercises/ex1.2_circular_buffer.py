class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size                     # creates the CircularBuffer class buffer holder
        self.next = 0                                   # sets next to 0
        self.oldest = 0                                 # sets oldest to 0

    def put(self, obj):                                 # makes a class method that takes an object
        next_item = (self.next + 1) % len(self.buffer)  # counts the next index. modulo will keep the counter between 0 and len(buffer) - 1
                                                        # keeps track of oldest number

        if self.buffer[self.next] is not None:          # if buffer number is taken, we need to replace old number
            self.oldest = next_item                     # makes oldest number the next number [1, 2, 3]  if next number is (1) old number is now 2

        self.buffer[self.next] = obj                    # replace buffer position at next one [1, 5, 3]
        self.next = next_item                           # set next item = 2 
                                                        # oldest number is the one getting replaced
    def get(self):
        value = self.buffer[self.oldest]                # this is the one we want to get
        self.buffer[self.oldest] = None                 # this is how we change it 
        if value is not None:                           #
            self.oldest += 1
            self.oldest %= len(self.buffer)

        return value
    
buffer = CircularBuffer(3)                              # [None, None, None]

print(buffer.get() is None)       # True                only increase the number if value is not none
buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)           # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

# # The above code should display True 15 times.