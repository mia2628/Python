def solution(numbers):
  num = []
    
  for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
      num.append(numbers[i] + numbers[j])
            
  num = list(set(num))
  num.sort()
  return num