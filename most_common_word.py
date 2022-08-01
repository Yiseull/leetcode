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