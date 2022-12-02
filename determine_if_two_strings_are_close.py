from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        myDict1 = Counter(word1)
        myDict2 = Counter(word2)

        mySet1 = set(myDict1.keys())
        mySet2 = set(myDict2.keys())

        myList1 = list(myDict1.values())
        myList2 = list(myDict2.values())

        myList1.sort()
        myList2.sort()

        return mySet1 == mySet2 and myList1 == myList2