def solution(strings, n):
    array1 = []
    array2 = []
    arr2 = []
    for i in range(len(strings)):
        array1.append(strings[i][n])
    array1.sort()

    for x in array1:
        for j in range(len(strings)):
            if strings[j][n] in x:
                array2.append(strings[j])
                for v in array2:
                    if v not in arr2:
                        arr2.append(v)

    for y in range(len(arr2)):
        min_index = y
        for k in range(y+1, len(arr2)):
            if arr2[min_index][n] == arr2[k][n] and arr2[min_index] >= arr2[k]:
                min_index = k
        arr2[min_index], arr2[y] = arr2[y], arr2[min_index]

    return arr2