from doubly_linked_list import DoublyLinkedList, ListNode

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
            # ANSWER: Push and Pop are have O(1) time complexity
        self.storage = None

    def push(self, value):
        if self.storage is None:
            self.storage = DoublyLinkedList(ListNode(value))
            self.size = self.storage.length

        else:
            self.storage.add_to_tail(value)
            self.size = self.storage.length

    def pop(self):
        if self.storage is None:
            return None

        else:
            node = self.storage.remove_from_tail()
            self.size = self.storage.length
            return node


    def len(self):
        return self.size
