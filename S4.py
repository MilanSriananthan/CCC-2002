group = int(input())
queue = int(input())
people = {}
allspeeds = []
for i in range(queue):
    name = input()
    speed = int(input())
    people[name] = speed
    allspeeds.append(speed)

allspeeds.sort()

def split()
