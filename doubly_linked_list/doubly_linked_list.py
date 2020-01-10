"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Find a node at a particular index."""

    def get_at(self, index):
        if self.head is None:
            return None

        counter = 0
        node = self.head

        while counter < index:
            if node is None:
                return None

            node = node.next
            counter += 1

        return node

    def add_at(self, index, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        elif index == 0:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
            next_node.prev = self.head

        else:
            next_node = self.get_at(index - 1)
            new_node.prev = next_node.prev
            next_node.prev = new_node
            new_node.next = next_node

        self.length += 1
        return new_node

    def remove_at(self, index):
        if self.head is None:
            return None

        elif index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        else:
            current_node = self.get_at(index - 1)
            if current_node is None or current_node.next is None:
                return None

            else:
                prev_node = current_node.prev
                current_node = current_node.next
                prev_node.next = current_node
                self.length -= 1
                return

    """Reset head and tail nodes to default"""

    def reset_head_and_tail(self):
        self.head = None
        self.tail = None

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = self.tail = new_node

        else:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
            next_node.prev = self.head

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        old_head = self.head
        if self.head is None or self.tail is None:
            return None

        elif self.length == 1:
            self.reset_head_and_tail()

        else:
            self.head = old_head.next

        self.length -= 1
        return old_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        # return self.tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        old_tail = self.tail
        if self.head is None or self.tail is None:
            return None

        elif self.length == 1:
            self.reset_head_and_tail()

        else:
            self.tail = old_tail.prev

        self.length -= 1
        return old_tail.value

    """Find node in the list"""

    def find_node(self, node):
        if self.head is None:
            return False
        elif self.head == node:
            return True
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
                if curr_node == node:
                    return True

            return False

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if self.find_node(node):
            temp_node = node
            next_node = self.head
            self.head = temp_node
            self.head.next = next_node
            next_node.prev = self.head

        else:
            return None

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.tail is None:
            return None
        if node is self.tail:
            return

        value = node.value
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)

        else:
            self.delete(node)
            self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.find_node(node):
            print("Node not found")
            return

        if node is self.head:
            self.remove_from_head()

        elif node is self.tail:
            self.remove_from_tail()

        elif self.head:
            curr_node = self.head.next
            index = 0
            while curr_node:
                curr_node = curr_node.next
                index += 1

            self.remove_at(index)

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.head is None:
            return None

        curr_node = self.head
        max_value = curr_node.value

        while curr_node.next:
            curr_node = curr_node.next
            if curr_node.value > max_value:
                max_value = curr_node.value

        return max_value

    def print_dll(self):
        if self.head is None:
            return None
        
        node = self.head
        print("dll contents:")
        while node:
            print(node.value)
            node = node.next

