# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        cnt = 0
        while node:
            node = node.next
            cnt += 1

        node = head
        for _ in range(cnt // 2):
            node = node.next

        return node