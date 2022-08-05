# 파이썬 알고리즘 인터뷰 solution Runtime: 107ms
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())