class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        stack = []
        s = list(s)

        for char in s:
            if char in vowels:
                stack.append(char)

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = stack.pop()

        return ''.join(s)