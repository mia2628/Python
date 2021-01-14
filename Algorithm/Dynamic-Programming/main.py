import time

start_time = time.time()
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(9))
end_time = time.time()
print('time :', end_time - start_time)


d = [0] * 1000
start_time = time.time()
def fibo(x):
  if x == 1 or x == 2:
    return 1
  
  if d[x]!= 0:
    return d[x]
  
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(999))
end_time = time.time()
print('time :', end_time - start_time)

d = [0] * 100

def pibo(x):
  print('f(' + str(x) + ')', end=' ')
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = pibo(x-1) + pibo(x-2)
  return d[x]
print(pibo(6))

#보텀업 - 상향식
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
  d[i] = d[i-1] + d[i-2]

print(d[n])