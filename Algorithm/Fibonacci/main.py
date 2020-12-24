n = int(input())

fb = [0] * (n + 1)
fb[1] = 1

for i in range(2, n + 1):
  fb[i] = fb[i - 1] + fb[i - 2]

print(fb[n])