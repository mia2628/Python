# # 입력을 위한 전형적인 코드
# n = int(input()) # 데이터의 개수 입력
# data = list(map(int, input().split())) # 각 데이터를 공백으로 구분하여 입력

# data.sort(reverse = True)
# print(data)

# # 공백을 기준으로 구분하여 적은 수의 데이터 입력
# n, m, k = map(int, input().split()) # n, m, k를 공백으로 구분하여 입력
# print(n, m, k)

# import sys
# data = sys.stdin.readline().rstrip()
# print(data)

# output
a = 1
b = 2
print(a,b)
print(a)
print(b)

#출력할 변수들
answer = 7
#print("정답은 " + answer + "입니다.") 에러
print("정답은 " + str(answer) + "입니다.")
print("정답은 ",str(answer), "입니다.")
print(f"정답은 {answer}입니다.") #f-string