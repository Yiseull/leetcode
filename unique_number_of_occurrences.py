from collections import Counter
from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        occurrences = set()

        for c in counter.values():
            if c in occurrences:
                return False
                break
            occurrences.add(c)

        return True