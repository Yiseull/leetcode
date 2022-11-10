class Solution1:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = []
        s = list(s)

        for char in s:
            if char in vowels:
                stack.append(char)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = stack.pop()

        return ''.join(s)

class Solution2:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return ''.join(s)
