N = int(input())

answer = 0

for i in range(N+1):
    for j in range(60):
        for z in range(60):
            if '3' in str(i) + str(j) + str(z):
                answer += 1
print(answer)





N = int(input())

answer = 0

for i in range(N+1):
    for j in range(60):
        for z in range(60):
            if ((i%10 == 3 or i//10 ==3) or (j//10 == 3 or j % 10 == 3) or
                (z // 10 == 3 or z% 10 == 3)):
                answer += 1
print(answer)