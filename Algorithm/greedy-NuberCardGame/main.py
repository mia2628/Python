# min 함수 사용
n, m = map(int, input().split()) # N,M을 공백으로 구분하여 입력받기

result = 0 # 결과값

for i in range(n): #한 줄씩 입력받아 확인
  data = list(map(int, input().split()))
  min_value = min(data) # 현재 줄에서 가장 작은수 찾기
  result = max(result, min_value) # 가장 작은수 들 중에서 가장 큰 수 찾기
print(result)

# 2중 반복문 사용
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value, a) # 현재 줄에서 가장 작은수 찾기
  result = max(result, min_value) # 가장 작은수 들 중에서 가장 큰 수 찾기

print(result)