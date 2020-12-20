#재귀함수로 표현
def fibo(x):
  if x == 1 or x ==2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(4))

#Memoization, Caching - 한 번 구한 정보를 리스트에 저장 - 그대로 리스트에서 가져옴
d = [0] *100 #한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

def fibo(x): #재귀함수 구현(탑다운 다이나믹 프로그래밍)
  if x == 1 or x == 2: #종료조건(1혹은 2일때 1반환)
    return 1
  if d[x] != 0: #이미 계산한적 있는 문제라면 그대로 반환
    return d[x]
  d[x] = fibo(x-1) + fibo(x-2) #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  return d[x]
print(fibo(99))