#stack
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop
stack.append(1)
stack.append(4)
stack.pop

print(stack)
print(stack[::-1])

#queue
from collections import deque
queue = deque() # 큐 구현을 위해 deque 라이브러리 사용
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#recursive function
def recursive_function():
  print('재귀 함수를 호출합니다.')
   recursive_function()

recursive_function()

#종료조건 설정했을 때
def recursive_function(i):
  if i == 100: #100번째 출력했을 때 종료되도록 종료 조건 명시
    return
  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀 함수를 종료합니다.')
recursive_function(1)

#factorial
#반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1): #1부터 n까지의 수를 차례대로 곱하기
    result *= i
  return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1: #n이 1 이하인 경우 1을 반환
    return 1
  return n * factorial_recursive(n-1)#n! = n * (n-1)를 그대로 코드로 작성하기

print('반복적으로 구현:', factorial_recursive(5))
print('재귀적으로 구현:', factorial_recursive(5))