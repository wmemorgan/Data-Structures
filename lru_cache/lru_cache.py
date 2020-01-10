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
        self.storage = None

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # print(f"LOOKING FOR KEY: {key}")
        if self.storage is None:
            return None

        curr_node = self.storage.storage.head
        while curr_node:
            if key in curr_node.value:
                self.storage.storage.move_to_end(curr_node)
                return curr_node.value[key]

            curr_node = curr_node.next

        return None

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
        if self.storage is None:
            self.storage = Queue()
            self.storage.enqueue({key: value})

        elif self.get(key):
            # print(f"key exists")
            #self.storage.storage.tail.value.update({key : value})
            self.storage.storage.tail.value[key] = value
            # print(f"NEW K,V: {self.storage.storage.tail.value}")

        else:
            self.checkLimit()
            self.storage.enqueue({key: value})


    def checkLimit(self):
        if self.storage.len() >= self.limit:
            self.storage.dequeue()

    def print_cache(self):
        if self.storage is None:
            print("Empty cache")

        node = self.storage.storage.head
        print("lru_cache contents:")
        while node:
            print(node.value)
            node = node.next

