n = int(input())
students = [] #학생 정보를 담을 리스트

for i in range(n):
  students.append(input().split())

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
  print(student[0])

