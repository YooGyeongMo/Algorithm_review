N = input()

i=0
while True:
    try:
        print(N[i],end="")
        i += 1
        if i % 10 == 0:
            print()
    except:
        break

i = 0
for char in N:
    i+=1
    print(char,end="")
    if i == 10:
        print()
        i = 0