from dll_queue import Queue

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = dict()
        self.order = Queue()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.storage:
            return None

        else:
            node = self.storage[key]
            self.order.storage.move_to_end(node)
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.storage.move_to_end(node)

        else:
            self.order.enqueue((key, value))
            self.storage[key] = self.order.storage.tail
            self.checkLimit()


    def checkLimit(self):
        if self.order.len() > self.limit:
            del self.storage[self.order.dequeue()[0]]
            

    def print_cache(self):
        if self.order.len() == 0:
            print("Empty cache")

        node = self.order.storage.head
        print("lru_cache contents:")
        while node:
            print(node.value)
            node = node.next

