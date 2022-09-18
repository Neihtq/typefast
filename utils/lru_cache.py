class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LRU_CACHE:
    def __init__(self, max_length):
        self.max_length = max_length
        self.length = 0
        self.head = Node(None)
        self.tail = self.head

    def insert(self, val):
        node = Node(val)
        if self.length == self.max_length:
            new_head = self.head.next.next
            to_del = self.head.next
            self.head.next = new_head
            del to_del
            self.length -= 1

        self.tail.next = node
        self.tail = node
        self.length += 1

    def peek_head(self):
        return self.head.next.val

    def peek_tail(self):
        return self.tail.val

    def show_all(self):
        curr = self.head.next
        content = []
        while curr:
            content.append(curr.val)
            curr = curr.next

        return content
