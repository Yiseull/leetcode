# 첫 번째 풀이 Runtime: 59ms
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

# 두 번째 풀이 Runtime: 694ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []
        for char in s:
            if char.isalnum():
                str.append(char.lower())

        # 팰린드롬 판별
        while len(str) > 1:
            if str.pop(0) != str.pop():
                return False

        return True