from dll_stack import Stack
from dll_queue import Queue

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Evaluate parent node
        if self.value is None:
            self.value = value

        # Edge case to address duplicate values
        if self.value == value:
            print(f"{value} exists")
            return

        # Evaluate left nodes
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # Evaluate right nodes
        if self.value < value:
            if self.right is None:    
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        # Base case
        if self.value is None:
            return False

        # Evaluate left nodes
        if self.value > target:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
                
        # Evaluate right nodes
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check for right nodes
        if self.right is None:
            # NO - return parent node value
            return self.value
        # YES - evaluate right subtrees
        else:
            subtree = self.right
            while subtree:
                if subtree.right is None:
                    return subtree.value
                else:
                    subtree = subtree.right
                
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left if you can
        if node.left:
            self.in_order_print(node.left)
        # print the current node
        print(node.value)
        # go right if you can
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue to keep track of nodes
        storage = Queue()
        # place the first node onto queue
        storage.enqueue(node)
        # while queue isn't empty:
        while storage.size > 0:
            # dequeue the top node
            curr_node = storage.dequeue()
            # print the node
            print(curr_node.value)
            # add children to the queue
            if curr_node.left:
                storage.enqueue(curr_node.left)
            if curr_node.right:
                storage.enqueue(curr_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack to keep track of nodes
        storage = Stack()
        # place the first node onto stack
        storage.push(node)
        # while stack isn't empty:
        while storage.size > 0:
            # pop the top node
            curr_node = storage.pop()
            # print the node
            print(curr_node.value)
            # add children to the stack
            if curr_node.right:
                storage.push(curr_node.right)
            if curr_node.left:
                storage.push(curr_node.left)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
print("for_each results:")
print_val = lambda x: print(x)
bst.for_each(print_val)
print("bst.in_order_print:")
bst.in_order_print(bst)
print("bst.bft_print:")
bst.bft_print(bst)
print("bst.dft_print:")
bst.dft_print(bst)
