# Defines Node Class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Defines Hashtable Class
class Hashtable:
    def __init__(self, beginningCapacity):
        self.capacity = beginningCapacity
        self.size = 0
        self.buckets = [None] * self.capacity

    # Defines Hash Function
    def hash(self, key):
        hashSum = 0
        hashSum = key % 10
        return hashSum

    # Defines insert object into Hashtable
    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None:
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)

    # Defines the find or lookup object in Hashtable
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:

            return None
        else:

            return node.value

    # Defines the function to delete object in Hashtable
    def delete(self, key):
        index = self.hash(key)

        node = self.buckets[index]

        while node.key != key:
            pre = node
            node = node.next

        if node is None:
            return None
        else:
            pre.next = pre.next.next

        return node.value;
