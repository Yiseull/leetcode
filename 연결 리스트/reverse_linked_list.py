# first solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while head:
            node, node.next, head = head, node, head.next

        return node