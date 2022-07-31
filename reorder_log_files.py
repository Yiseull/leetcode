# 첫 번째 풀이 Runtime: 29ms
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    let = []
    dig = []
    for log in logs:
        if log[log.find(' ') + 1].isalpha():
            let.append(log)
        else:
            dig.append(log)
    let.sort(key = lambda x: (x[x.find(' ') + 1:], x))
    return let + dig

# 두 번째 풀이: find() 대신 split() 사용. Runtime: 36ms
 def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let, dig = [], []
        for log in logs:
            if log.split()[1].isalpha():
                let.append(log)
            else:
                dig.append(log)
        let.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return let + dig