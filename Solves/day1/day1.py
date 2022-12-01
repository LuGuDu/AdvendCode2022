f = open("input.txt", "r")

#PART 1
sum = 0
sumMayor = 0
sumActual = 0
for i in f.readlines():
    if i != "\n":
        sum = sum + int(i)
        continue
    
    sumActual = sum
    if sumActual > sumMayor:
        sumMayor = sumActual
    sum = 0
print(sumMayor)


f = open("input.txt", "r")

#PART 2
sum = 0
sumMayor = 0
sumMayor2 = 0
sumMayor3 = 0
sumActual = 0
for i in f.readlines():
    if i != "\n":
        sum = sum + int(i)
        continue
    
    sumActual = sum
    sumAuxiliar = 0
    if sumActual > sumMayor:
        sumMayor3 = sumMayor2
        sumMayor2 = sumMayor
        sumMayor = sumActual
    elif sumActual > sumMayor2:
        sumMayor3 = sumMayor2
        sumMayor2 = sumActual
    elif sumActual > sumMayor3:
        sumMayor3 = sumActual
    sum = 0
print(sumMayor + sumMayor2 + sumMayor3)

# 69206
# 197400