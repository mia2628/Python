# while문 이용
n, m, k = map(int, input().split()) # N, M, K를 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받기

data.sort() # 입력받은 수 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

import time
start_time = time.time() # 측정 시작

while True:
  for i in range(k): # 가장 큰 수를 K번 더하기
    if m == 0:
      break # m이 0이라면 반복문 탈출
    result += first
    m -= 1 # 더할 때마다 1씩 빼기
  if m == 0 :
    break # m이 0이라면 반복문 탈출
  result += second # 두 번째로 큰 수를 한 번 더하기
  m -= 1 # 더할 때마다 1씩 빼기
end_time = time.time()
print("시간 제한 : ", end_time - start_time)
print(result)


# 수열 이용
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 정렬
first = data[n-1]
second = data[n-2]

start_time = time.time() # 측정 시작
count = int( m / ( k + 1 )) * k # 가장 큰 수가 더해지는 횟수 계산
count += m % ( k + 1 ) # 나눠서 떨어지지 않았을 때 가장 큰 수가 더해지는 횟수 계산

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기
end_time = time.time()
print("시간 제한 :", end_time - start_time)
print(result)