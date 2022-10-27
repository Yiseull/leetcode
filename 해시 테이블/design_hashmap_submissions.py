import collections

class MyHashMap:

    def __init__(self):
        self.dic = collections.defaultdict()

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value

    def get(self, key: int) -> int:
        if self.dic.get(key) is None:
            return -1
        return self.dic.get(key)

    def remove(self, key: int) -> None:
        if self.dic.get(key) is not None:
            del self.dic[key]