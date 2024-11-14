N = int(input())

count = 0

for i in range(N+1):
    for j in range(60):
        for z in range(60):
            # z_sib = z//10
            # z_seconds = z%10
            # j_sib = j//10
            # j_seconds = j%10
            # if i==3 or j_seconds==3 or j_sib == 3 or z_seconds == 3 or z_sib == 3:
            #     count += 1
            if '3' in str(i)+str(j)+str(z):
                count +=1

print(count)