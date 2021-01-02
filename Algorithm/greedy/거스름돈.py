n = int(input())

count = 0
coin_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for coin_type in coin_types:
    count += (n // coin_type)
    n -= (n // coin_type * coin_type)
    if (n == 0):
      break
    
print(count)
