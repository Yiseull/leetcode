# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # my solution, Runtime: 62ms
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        node1, node2, node3 = list1, list2, list3

        while node1 or node2:
            if node1 is None:
                while node2:
                    node3.next = ListNode()
                    node3 = node3.next
                    node3.val = node2.val
                    node2 = node2.next
                break

            if node2 is None:
                while node1:
                    node3.next = ListNode()
                    node3 = node3.next
                    node3.val = node1.val
                    node1 = node1.next
                break

            node3.next = ListNode()
            node3 = node3.next
            if node1.val < node2.val:
                node3.val = node1.val
                node1 = node1.next
            else:
                node3.val = node2.val
                node2 = node2.next

        return list3.next

    # 파이썬 알고리즘 인터뷰 solution, Runtime: 42ms
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1