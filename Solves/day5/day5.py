f = open("input.txt", "r")

stacks = [[], [], [], [], [], [], [], [], []]
cont = 0
for i in f.readlines():
    if (cont >= 10):
        i = i.strip().split(" ")
        iterations = int(i[1])
        origin = int(i[3])-1
        destination = int(i[5])-1

        auxiliarStack = list()

        for a in range(iterations):
            order = iterations-a
            if(len(stacks[origin]) != 0):
                element = stacks[origin].pop()
                auxiliarStack.append(element)
            else:
                continue
        auxiliarStack = auxiliarStack[::-1]
        for el in auxiliarStack:
            stacks[destination].append(el)
        
    elif(cont <= 7):
        i = list(i)
        index=0
        for a in range(1, 34, 4):
            stacks[index].append(i[a]) if (i[a] != " ") else 0
            index += 1
    elif(cont == 9):
        for a in range(9):
            stacks[a] = stacks[a][::-1]
    cont += 1

string = ""
for s in stacks:
    string += s[-1]
print(string)