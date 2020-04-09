case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]

result = [a+b for a in case_1 for b in case_2]
print(result)

case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "F"]

result = [[a+b for a in case_1] for b in case_2]
print(result)
