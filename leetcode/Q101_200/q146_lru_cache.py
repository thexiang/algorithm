# LeetCodeUrl: https://leetcode.com/problems/lru-cache/
# Question Name: 146. LRU Cache
# Time Complexity: N/A
# Space Complexity: N/A
# Tag: Linked List

class DoublyLinkedListNode():
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    A least recently used (LRU) cache implemented using a doubly linked list and dictionary

    Attributes:
        capacity (int): Maximum number of items the cache can hold.
        cache (dict): A dictionary to hold cached items.
        size (int): Current size of the cache.
        head (DoublyLinkedListNode): The head sentinel node of the doubly linked list.
        tail (DoublyLinkedListNode): The tail sentinel node of the doubly linked list.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.head, self.tail = DoublyLinkedListNode(), DoublyLinkedListNode()

        self.head.next = self.tail
        self.tail.prev = self.head



    def _add_node(self, node: DoublyLinkedListNode):
        """Adds a node right after the head of the doubly linked list."""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DoublyLinkedListNode):
        """Removes a node from the doubly linked list."""
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def _move_node_to_start(self, node: DoublyLinkedListNode):
        """Moves a specific node to the beginning (right after the head) of the doubly linked list."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DoublyLinkedListNode:
        """Removes and returns the node right before the tail of the doubly linked list."""
        res = self.tail.prev
        self._remove_node(res)
        return res


    def get(self, key: int) -> int:
        """Get the value of the node with the given key if it exists in the lru cache."""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_node_to_start(node)
        

        return node.value

    def put(self, key: int, value: int) -> None:
        """Add a new node with the given key and value to the lru cache, or update an existing one."""
        # if the key in the cache, we move it to the head
        if key in self.cache:
            node = self.cache[key]  # update the cache
            node.value = value  # update the new value
            self._move_node_to_start(node)
            return

        # if cache miss, then make a new node, and add it to the head
        new_node = DoublyLinkedListNode(key=key, value=value)
        self._add_node(new_node)
        self.cache[key] = new_node
        self.size += 1
 
        if self.size <= self.capacity:
            return

        # clean up the tail node if it's over capacity
        tail = self._pop_tail()
        del self.cache[tail.key]
        self.size -= 1
