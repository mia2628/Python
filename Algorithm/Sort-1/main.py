#k번째 수
n, k = map(int, input().split())
a = list(map(int, input().split()))

result = sorted(a)
print(result[k-1])

#수 정렬1
n = int(input())
ls = []

for _ in range(n):
  ls.append(int(input()))

s = sorted(ls)

for i in s:
  print(i)

#수 정렬2
n = int(input())
ls = []

for _ in range(n):
  ls.append(int(input()))

s = sorted(ls)

for i in s:
  print(i)

#수 정렬3(입력 순서 거꾸로)
n = int(input())
ls = []

for i in range(n):
  ls.append(int(input()))

for i in reversed(ls):
  print(i)