f = open("input.txt", "r")

sum = 0
sumMayor = 0
sumActual = 0
for i in f.readlines():
    i =+ sum
    if i == "":
        sumActual = sum
        if sumActual < sumMayor:
            sumMayor = sumActual

print(sumMayor)

