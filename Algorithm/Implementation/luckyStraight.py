def luckyStraight(n):

  n = str(n)
  left = 0
  right = 0

  for i in range(len(n)//2):
    left += int(n[i])
    right += int(n[(len(n)//2)+i])

  if left == right:
    return 'LUCKY'
  else:
    return 'READY'

print(luckyStraight(7755))