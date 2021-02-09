from random import randint
array = []
for i in range(0, 100):
  array_num = randint(1, 10)
  array.append(array_num)
count = [0] * (max(array)+1)

for j in range(len(array)):
  count[array[j]] += 1

for j in range(len(count)):
  for k in range(count[j]):
    print(j, end='')

#py sorted
array_sorted = [7,6,3,5,1,2,5,6,7,0,1]
result = sorted(array_sorted)
print(result)

array_sort = [1,5,7,1,3,5,1,6,7,7,0,2]
array_sort.sort()
print(array_sort)

array_key = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
  return data[1]
result = sorted(array_key, key=setting)
print(result)