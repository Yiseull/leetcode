class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(), ListNode()
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            node = ListNode(value)
            self.head.right, node.right = node, self.head.right
            node.left, node.right.left = self.head, node
            return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            node = ListNode(value)
            self.tail.left, node.left = node, self.tail.left
            node.right, node.left.right = self.tail, node
            return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            node = self.head.right
            self.head.right, node.right.left = node.right, self.head
            node = None
            return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            node = self.tail.left
            self.tail.left, node.left.right = node.left, self.tail
            node = None
            return True

    def getFront(self) -> int:
        return -1 if self.len == 0 else self.head.right.val

    def getRear(self) -> int:
        return -1 if self.len == 0 else self.tail.left.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k