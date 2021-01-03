pasta1 = int(input())
pasta2 = int(input())
pasta3 = int(input())
juice1 = int(input())
juice2 = int(input())

pasta_list = [pasta1, pasta2, pasta3]
juice_list = [juice1, juice2]
price_list= []

for x in pasta_list:
    for y in juice_list:
        price_list.append(x + y + ((x + y) * 0.1))

price_list = sorted(price_list)
print(price_list[0])
