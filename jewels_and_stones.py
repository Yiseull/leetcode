import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = collections.Counter(stones)
        result = 0

        for jewel in jewels:
            if (stones_dict.get(jewel) is not None):
                result += stones_dict.get(jewel)

        return result