#greedy
n = 1260 # 거스름돈이 1260원
count = 0 

#큰 단위의 화폐부터 차례대로 확인
count_types = [500, 100, 50, 10]

for coin in count_types:
  count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
  n %= coin # 큰 화폐부터 거슬러 주고 남은 거스름돈

print(count)


# n = 1260 # 거스름돈이 1260원
# count = 0 
# count += n // 500
# print (count)
# n %= 500
# print(n)