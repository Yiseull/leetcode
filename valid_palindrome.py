# 첫 번째 풀이: 일일이 비교, Runtime: 59ms
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[left].lower() != s[right].lower():
                        return False
                    else:
                        right -= 1
                        left += 1
                else:
                    right -= 1
            else:
                if s[right].isalnum() == 1:
                    left += 1
                else:
                    right -= 1
                    left += 1
        return True

# 두 번째 풀이: 데크 자료형 이용, Runtime: 69ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 판별
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

# 세 번째 풀이: 슬라이싱 사용, Runtime: 54ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]