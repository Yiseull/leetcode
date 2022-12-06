from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = Counter(word1)
        dict2 = Counter(word2)

        return dict1.keys() == dict2.keys() and sorted(dict1.values()) == sorted(dict2.values())