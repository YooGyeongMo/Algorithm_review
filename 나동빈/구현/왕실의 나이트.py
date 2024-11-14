N = input()

x = (ord(N[0])%97 + 1) - 1
y = int(N[1]) - 1

data_list = [[-1,-2],[1,-2],[-1,2],[1,2],[2,-1],[2,1],[-2,-1],[-2,1]]

count = 0

for i in range(8):
    nx = x + data_list[i][0]
    ny = y + data_list[i][1]
    if 0 <= nx < 8 and 0 <= ny < 8:
        count += 1


print(count)
