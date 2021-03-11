def solution(A):
    d = {}
    for x in A:
        d[x] = d.get(x, 0) + 1
    result = [k for k, v in d.items() if v >= 1]
    return len(result)