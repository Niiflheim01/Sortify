class Array:
    """Wrapper for Python list to represent an array."""
    def __init__(self, data):
        self.data = list(data)

    def __getitem__(self, idx):
        return self.data[idx]

    def __setitem__(self, idx, value):
        self.data[idx] = value

    def __len__(self):
        return len(self.data)

    def to_list(self):
        return list(self.data)


class LinkedListNode:
    """Node for singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Singly linked list implementation."""
    def __init__(self, data):
        self.head = None
        self._length = 0
        prev = None
        for value in data:
            node = LinkedListNode(value)
            if not self.head:
                self.head = node
            else:
                prev.next = node
            prev = node
            self._length += 1

    def __len__(self):
        return self._length

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result 