from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # ANSWER: enqueue and dequeue have O(1) time complexity
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        if self.storage.length == 0:
            self.storage.add_to_head(value)

        else:
            self.storage.add_to_tail(value)

        self.size = self.storage.length

    def dequeue(self):
        if self.storage.head is None:
            return None

        else:
            head = self.storage.remove_from_head()
            self.size = self.storage.length
            return head

    def len(self):
        return self.size
