from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # solution1: 반복 구조로 스왑, Runtime: 51ms
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        prev.next = head

        while head and head.next:
            # swap
            b = head.next
            head.next = b.next
            b.next = head

            head, prev.next, prev = head.next, b, head

        return root.next

    # solution2: 재귀 구조로 스왑, Runtime: 54ms
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head