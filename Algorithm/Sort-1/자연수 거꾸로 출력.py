def solution(n):
    
    n = str(n)
    result_str = []
    result_int = []
    for i in range(len(n)):
        result_str.append(n[i])
        result_int.append(int(result_str[i]))

    start = 0
    end = len(result_int)-1
    while start < end:
        result_int[start], result_int[end] = result_int[end], result_int[start]
        start += 1
        end -= 1
        
        
    return result_int
