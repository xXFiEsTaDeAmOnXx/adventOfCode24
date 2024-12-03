import re

data = None

with open("input.txt", "r") as file:
    data = file.read()

res = re.findall(r"(do\(\))|(mul\(\d{1,3},\d{1,3}\))|(don't\(\))", data)

sum = 0
is_do = True
for op in res:
    if op[0] == "do()":
        is_do = True
    elif op[2] == "don't()":
        is_do = False
    else:
        if is_do:
            num1, num2 = re.findall(r"\d{1,3}", op[1])
            sum += int(num1) * int(num2)

print(sum)
