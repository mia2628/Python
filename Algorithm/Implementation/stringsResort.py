n = input()
strings_list = []
num_list = []
result = 0

for i in range(len(n)):
  try:
    int(n[i]) == True
    num_list.append(n[i])
  except:
    strings_list.append(n[i])

strings_list.sort()
for j in num_list:
  result += int(j)

strings = "".join(strings_list)

print(strings, end='')
print(result)