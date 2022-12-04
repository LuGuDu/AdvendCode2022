f = open("input.txt", "r")

points1 = 0
points2 = 0
for i in f.readlines():
    areas=i.split(",")
    area1 = areas[0].split("-")
    area2 = areas[1].split("-")

    a1x = int(area1[0])
    a1y = int(area1[1])
    a2x = int(area2[0])
    a2y = int(area2[1].strip())
    
    #PART 1
    if ((a1x >= a2x and a1y <= a2y) or (a2x >= a1x and a2y <= a1y)):
        points1 += 1
    
    #PART 2
    if ((a1y >= a2x and a1y <= a2y) or (a2y >= a1x and a2y <= a1y)):
        points2 += 1

print(points1)
print(points2)