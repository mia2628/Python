n = int(input())

#별찍기
count = 0
for i in range(0,n):
  print('*'*(i+1))
  if i == (n-1):
    for i in range((n+1),1,-1):
      print('*'*(i-1))


#반대로 별찍기
count = 0
for i in range(0,n):
  print(' '*(n-i), '*'*(i+1),'*'*(i+1), ' '*(n-i))
for j in range(0,n):
    print(' '*(j+1), '*'*(n-j),'*'*(n-j), ' '*(j))
