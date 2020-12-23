top = int(input())
bottom = int(input())

whole = top // bottom

top -= whole*bottom

#print(whole)
#print(bottom)

def greatest(num1, num2):
    result = 0
    for i in range(num1, 0, -1):
        first = num1/i
        second = num2/i
        if wholenumber(first) == True and wholenumber(second) == True:
            result = [int(first),int(second)]
            break
    return result

def wholenumber(num):
    if int(num) == num:
        return True
    return False

if top == 0 and whole == 0:
    print(0)
elif top == 0:
    print(whole)
else:
    answer = greatest(top, bottom)
    if whole == 0:
        print(str(answer[0]) + "/" + str(answer[1]))
    else:
        print(str(whole) + " " + str(answer[0]) + "/" + str(answer[1]) )
