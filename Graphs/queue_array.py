
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.num_items = 0
        self.front = 0
        self.rear = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError
        if self.is_empty():
            self.rear = self.rear
            self.front = self.rear
        elif self.rear +1 == self.capacity:
            self.rear = 0
        else:
            self.rear += 1
        self.items[self.rear] = item
        self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError
        temp = self.items[self.front]
        self.items[self.front] = None
        if self.front + 1 == self.capacity:
            self.front = 0
        else:
            self.front += 1
        self.num_items -= 1
        return temp

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
