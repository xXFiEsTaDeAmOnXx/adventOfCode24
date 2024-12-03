import re

data = None

with open("input.txt", "r") as file:
    data = file.read()


res = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)

sum = 0
for mul in res:
    num1, num2 = re.findall(r"\d{1,3}", mul)
    sum += int(num1) * int(num2)

print(sum)
