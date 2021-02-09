#선택정렬
from random import randint
array =[]
for j in range(0, 100):
  array_num = randint(1, 100)
  array.append(array_num)

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[min_index], array[i] = array[i], array[min_index] #스와프
print(array)
