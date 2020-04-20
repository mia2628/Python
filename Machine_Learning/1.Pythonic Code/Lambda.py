# Lambda
# 함수 이름 없이 함수처럼 쓸 수 있는 익명함수
# 수학의 람다대수에서 유래
#
# def f(x,y):
#     return x+y
#
# print(f(1,2))

# f = lambda x,y: x+y
# (f(1,2))
#
# # Map sequence
# ex = [1,2,3,4,5]
# f = lambda x:x ** 2
# list(map(f,ex))
#
# ex = [1,2,3,4,5]
# f = lambda x,y: x+y
# list(map(f,ex,ex))
#
# list(map(lambda x: x ** 2 if x % 2 == 0 else x,ex))
#
# [value ** 2 for value in ex]

# #Map Reduce
# from functools import reduce
# reduce(lambda x,y : x+y, [1,2,3,4,5])
#
# def factorial(n) :
#     return reduce(lambda x,y : x*y, range(1, n+1))
#
# factorial(5)
