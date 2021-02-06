#삽입정렬
from random import randint

array = []
for k in range(1,100):
  array_num = randint(1,100)
  array.append(array_num)

for i in range(1, len(array)):
  for j in range(i, 0 ,-1):
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else:
      break
print(array)