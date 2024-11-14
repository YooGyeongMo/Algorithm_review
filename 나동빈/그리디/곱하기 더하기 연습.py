N = input()

result = 0

for i in range(0,len(N)):
    num = int(N[i])
    if num <= 1 or result <= 1 :
        result += num
    else:
        result *= num

print(result)