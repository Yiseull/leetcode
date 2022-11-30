from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = [[] for _ in range(2)]
        counter = defaultdict(int)

        for match in matches:
            if counter[match[0]]:
                pass
            counter[match[1]] += 1

        for key in counter:
            if counter[key] == 0:
                answer[0].append(key)
            elif counter[key] == 1:
                answer[1].append(key)

        answer[0].sort()
        answer[1].sort()
        return answer