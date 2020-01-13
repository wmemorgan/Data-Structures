from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
            # ANSWER: Push and Pop have O(1) time complexity
        self.storage = DoublyLinkedList()

    def push(self, value):
        if self.storage.length == 0:
            self.storage.add_to_head(value)

        else:
            self.storage.add_to_tail(value)
        
        self.size = self.storage.length

    def pop(self):
        if self.storage.tail is None:
            return None

        else:
            tail = self.storage.remove_from_tail()
            self.size = self.storage.length
            return tail


    def len(self):
        return self.size
