def plus(a, b):
  if a !== int():
    a = int(a);
    if b !== int():
      b = int(b);
      return a + b;

a_plus = plus(2,3)
print(a_plus)

def minus(a, b):
  return a - b;

a_minus = minus(2,3)
print(a_minus)

def time(a, b):
  return a * b;

a_time = time(2,3)
print(a_time)

def division(a, b):
  return a / b;

a_div = division(2,3)
print(a_div)

def negation(a, b):
  return a // b;

a_neg = negation(2,3)
print(a_neg)

def power(a, b):
  return a ** b;

a_pow = power(2,3)
print(a_pow)
