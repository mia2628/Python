#순차탐색
def sequential_search(n, target, array):
  for i in range(n): #각 원소를 하나씩 확인
    if array[i] == target: #현재의 원소가 찾고자 하는 원소와 동일한 경우
      return i + 1 #현재의 위치 반환(인덱스는 0부터 시작하기 때문에 1 더해줌)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) #원소의 개수
target = input_data[1] #찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array)) #순차탐색 수행 결과 출력