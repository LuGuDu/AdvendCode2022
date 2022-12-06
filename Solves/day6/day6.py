f = open("input.txt", "r")

#PART 1
package = list()
line = f.readline()
line = list(line)
for index in range(0,len(line)-1):
    package.append(line[index])
    package.append(line[index+1])
    package.append(line[index+2])
    package.append(line[index+3])
    myunique = set(package)
    if len(myunique) == 4:
        print(myunique)
        print(index+4)
        break
    else:
        package.clear()

#PART 2
package = list()
for index in range(0,len(line)-1):
    for cont in range(14):
        package.append(line[index+cont])
    myunique = set(package)
    if len(myunique) == 14:
        print(myunique)
        print(index+14)
        break
    else:
        package.clear()
