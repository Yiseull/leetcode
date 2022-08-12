# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # first solution: deque 이용, Runtime: 1002ms
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dq = collections.deque()

        if not head:
            return True

        node = head
        while node:
            dq.append(node.val)
            node = node.next

        while len(dq) > 1:
            if dq.pop() != dq.popleft():
                return False

        return True

    # second solution: Runner를 이용한 우아한 풀이, Runtime: 784ms
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev