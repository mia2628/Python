def solution(N):
    
    value = bin(N)[2:]
    
    my_list = []
    space = 0
    for i in value:
        if i == '0':
            space += 1
        else:
            my_list.append(space)
            space = 0
    return value


print(solution(1005))