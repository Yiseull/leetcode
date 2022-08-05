# 첫 번째 풀이 Runtime: 44ms
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z]', ' ', paragraph.lower())
        paragraph = paragraph.split()

        words = set(paragraph)
        for ban in banned:
            if ban in words:
                words.remove(ban)

        result = ''
        cnt = 0
        for word in words:
            if cnt < paragraph.count(word):
                cnt = paragraph.count(word)
                result = word

        return result

    # 두 번째 풀이 Runtime: 36ms
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

