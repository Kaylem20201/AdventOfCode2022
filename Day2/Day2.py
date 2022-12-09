with open('input.txt') as f:
    lines = f.readlines()

score1 = 0
score2 = 0

for line in lines:
    chars = line.split()
    #Part 1:
    dif = ord(chars[1])-ord(chars[0])
    if dif == 23 : score1 += 3 #draw
    if dif == 24 or dif == 21 : score1 += 6 #win, X beats C
    score1 += ord(chars[1]) - 87 #X=1,Y=2,Z=3
    #Part 2:
    score2 += (ord(chars[1]) - 88)*3 #X=0,Y=3,Z=6
    if chars[1] == 'X': #Lose
        score2 += ord(chars[0])%3 + 1 #A=3,B=1,C=2
    if chars[1] == 'Y': #Draw
        score2 += ord(chars[0])-64 #A=1,B=2,C=3
    if chars[1] == 'Z': #Win
        score2 += (ord(chars[0])-1)%3 + 1 #A=2,B=3,C=1

print("Part 1: " + str(score1))
print("Part 2: " + str(score2))
