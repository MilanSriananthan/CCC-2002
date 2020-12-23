pink = int(input())
green = int(input())
red = int(input())
orange = (int(input()))
task = int(input())
count = []

pinksum = task // pink
greensum = task // green
redsum = task // red
orangesum = task // orange
total = 0

for i in range(orangesum + 1):
    total = i*orange
    for x in range(redsum + 1):
        newtotal = total + x*red
        for p in range(greensum + 1):
            aftertotal = newtotal +  p*green
            for z in range(pinksum + 1):
                finaltotal = aftertotal + z*pink
                if finaltotal == task:
                    here = [z, p, x, i]
                    count.append(here)


for i in count:
    print("# of PINK is " + str(i[0]) + ' # of GREEN is  ' + str(i[1])  + ' # of RED is ' + str(i[2]) + ' # of ORANGE is ' + str(i[3]))

print("Total combinations is " + str(len(count)) + ".")

save = 9999999999999999999999999999
for i in count:
    if save > sum(i):
        save = sum(i)

print("Minimum number of tickets to print is " + str(save) + ".")