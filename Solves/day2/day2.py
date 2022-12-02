f = open("input.txt", "r")

points = 0
for i in f.readlines():
    i.split(" ")
    p1 = i[0] #A-Rock; B-Paper; C-Scissors
    p2 = i[2] #X-Rock; Y-Paper; Z-Scissors

    #Loss
    if (p1=="A" and p2 == "Z") or (p1=="B" and p2=="X") or (p1=="C" and p2=="Y"):
        points += 0
    #Draw
    elif (p1=="A" and p2 =="X") or (p1=="B" and p2=="Y") or (p1=="C" and p2=="Z"):
        points += 3
    #Win
    elif (p1=="A" and p2 == "Y") or (p1=="B" and p2=="Z") or (p1=="C" and p2=="X"):
        points += 6
    
    if(p2=="X"):
        points += 1
    elif(p2=="Y"):
        points += 2
    elif(p2=="Z"):
        points += 3

print("Points: ", points)


#PART 2

f = open("input.txt", "r")

points = 0
for i in f.readlines():
    i.split(" ")
    p1 = i[0] #A-Rock; B-Paper; C-Scissors
    p2 = i[2] #X-Loss; Y-Draw; Z-Win

    if(p2=="X"):
        points += 0
    elif(p2=="Y"):
        points += 3
    elif(p2=="Z"):
        points += 6

    #Chosse rock
    if (p1=="A" and p2=="Y") or (p1=="B" and p2=="X") or (p1=="C" and p2=="Z"):
        points += 1
    #Choose paper
    elif (p1=="B" and p2=="Y") or (p1=="C" and p2=="X") or (p1=="A" and p2=="Z"):
        points += 2
    #Choose scissor
    elif (p1=="C" and p2=="Y") or (p1=="A" and p2=="X") or (p1=="B" and p2=="Z"):
        points += 3


    

print("Points: ", points)