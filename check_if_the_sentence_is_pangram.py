class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = set()

        for letter in sentence:
            pangram.add(letter)

        for i in range(97, 123):
            if chr(i) not in pangram:
                return False

        return True