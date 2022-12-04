f = open("input.txt", "r")


#PART 1
points = 0
for i in f.readlines():
    cad1 = i[:int((len(i)/2))]
    cad2 = i[int((len(i)/2)):]
    letter = set(cad1).intersection(cad2)
    letter = list(next(iter(letter)))
    char = letter[0]
    if(char.isupper()):
        points += ord(char)-38
    elif(char.islower()):
        points += ord(char)-96

print(points)


#PART 2
f = open("input.txt", "r")
points = 0
count = 0
cads = list()
for i in f.readlines():
    cads.append(i)
    count += 1

    if count >= 3:
        print(cads)
        intersection1 = set(cads[0].strip()).intersection(cads[1].strip())
        intersection2 = set(cads[0].strip()).intersection(cads[2].strip())
        intersection3 = intersection1.intersection(intersection2)

        letter = list(next(iter(intersection3)))
        char = letter[0]
        if(char.isupper()):
            points += ord(char)-38
        elif(char.islower()):
            points += ord(char)-96

        count = 0
        cads.clear()
        continue
    

print(points)
