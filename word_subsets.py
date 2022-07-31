def wordSubsets(words1, words2):
    result = []
    for i in words1:
        include = 1
        for j in words2:
            if j not in i:
                include = 0
                break
        if include == 1:
            result.append(i)
    return result
