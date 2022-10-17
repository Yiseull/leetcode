class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check = [False] * 26

        for char in (sentence):
            i = ord(char) - 97
            if check[i]:
                continue
            else:
                check[i] = True

        for c in check:
            if not c:
                return False

        return True
