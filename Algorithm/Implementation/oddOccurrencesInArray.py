# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    count = [0] * 100
    for i in A:
        count[i] += 1
    result = [x for x in count if x % 2 == 1]
    answer = count.index(result[0])
    return answer

print(solution([9,9,9,9,9,5,3,3,9]))