# A Queue abstract data type
#
# Written by Eric Martin for COMP9021


class EmptyQueueError(Exception):
    def __init__(self, message):
        self.message = message


class ArrayQueue:
    min_capacity = 10

    def __init__(self, capacity = min_capacity):
        self.min_capacity = capacity
        self._data = [None] * capacity
        self._length = 0
        self._front = 0
        
    def __len__(self):
        '''
        >>> len(ArrayQueue(100))
        0
        '''
        return self._length

    def is_empty(self):
        return self._length == 0

    def peek_at_front(self):
        '''
        >>> queue = ArrayQueue()
        >>> queue.peek_at_front()
        Traceback (most recent call last):
        ...
        EmptyQueueError: Cannot peek at front of empty queue
        '''
        if self.is_empty():
            raise EmptyQueueError('Cannot peek at front of empty queue')
        return self._data[self._front]

    def peek_at_back(self):
        '''
        >>> queue = ArrayQueue()
        >>> queue.peek_at_back()
        Traceback (most recent call last):
        ...
        EmptyQueueError: Cannot peek at back of empty queue
        '''
        if self.is_empty():
            raise EmptyQueueError('Cannot peek at back of empty queue')
        return self._data[(self._front + self._length - 1) % len(self._data)]

    def enqueue(self, datum):
        '''
        >>> queue = ArrayQueue(1)
        >>> queue.enqueue(0)
        >>> queue.peek_at_back()
        0
        >>> print(len(queue._data))
        1
        >>> queue.enqueue(1)
        >>> queue.peek_at_back()
        1
        >>> print(len(queue._data))
        2
        >>> queue.enqueue(2)
        >>> queue.peek_at_back()
        2
        >>> print(len(queue._data))
        4
        >>> queue.enqueue(3)
        >>> queue.peek_at_back()
        3
        >>> print(len(queue._data))
        4
        >>> queue.enqueue(4)
        >>> queue.peek_at_back()
        4
        >>> print(len(queue._data))
        8
        '''
        if self._length == len(self._data):
            self._resize(2 * len(self._data))
        self._data[(self._front + self._length) % len(self._data)] = datum
        self._length += 1

    def dequeue(self):
        '''
        >>> queue = ArrayQueue(4)
        >>> for i in range(8, -1, -1): queue.enqueue(i)
        >>> print(len(queue._data))
        16
        >>> print(queue.dequeue())
        8
        >>> print(len(queue._data))
        16
        >>> print(queue.dequeue())
        7
        >>> print(len(queue._data))
        16
        >>> print(queue.dequeue())
        6
        >>> print(len(queue._data))
        16
        >>> print(queue.dequeue())
        5
        >>> print(len(queue._data))
        16
        >>> print(queue.dequeue())
        4
        >>> print(len(queue._data))
        8
        >>> print(queue.dequeue())
        3
        >>> print(len(queue._data))
        8
        >>> print(queue.dequeue())
        2
        >>> print(len(queue._data))
        4
        >>> print(queue.dequeue())
        1
        >>> print(len(queue._data))
        4
        >>> print(queue.dequeue())
        0
        >>> print(len(queue._data))
        4
        >>> print(queue.dequeue())
        Traceback (most recent call last):
        ...
        EmptyQueueError: Cannot dequeue from empty queue
        '''
        if self.is_empty():
            raise EmptyQueueError('Cannot dequeue from empty queue')
        datum_at_front = self._data[self._front]
        # Not necessary, only done to possibly hasten garbage collection
        # of element being removed from the deque.
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)        
        self._length -= 1
        self._shrink_if_needed()
        return datum_at_front

    def _resize(self, new_size):
        # In any case, the element at position self._front will be at position 0 in new list.
        end = self._front + new_size
        # We are shrinking to a smaller list, and not wrapping in original list.
        if end <= len(self._data):
            self._data = self._data[self._front: end]
        # We are shrinking to a smaller list, but wrapping in original list.
        elif new_size <= len(self._data):
            # There are len(self._data) - self._front data in self._data[self._front: ],
            # and new_size - (len(self._data) - self._front) == end - len(self._data).
            self._data = self._data[self._front: ] + self._data[: end - len(self._data)]
        # We are expanding to a larger list.
        else:
            # The first two lists have a total length of len(self._data).
            self._data = (self._data[self._front: ] + self._data[: self._front] +
                          [None] * (new_size - len(self._data)))
        self._front = 0

    def _shrink_if_needed(self):
        # When the queue is one quarter full, we reduce its size to make it half full,
        # provided that it would not reduce its capacity to less than the minimum required.
        if self.min_capacity // 2 <= self._length <= len(self._data) // 4:
            self._resize(len(self._data) // 2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()    

        
