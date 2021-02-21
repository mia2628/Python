n = int(input())
array = list(map(int, input().split()))
array.reverse() #순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환

dp = [1] * n #dp 테이블

#가장 긴 증가하는 부분수열(LIS) 알고리즘 수행
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

#열외시켜야 하는 병사의 최소 수를 출력
print(dp)