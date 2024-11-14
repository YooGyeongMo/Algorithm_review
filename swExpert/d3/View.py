T = 10

for test_case in range(1,T+1):

    N = int(input())

    building = list(map(int,input().split()))

    result = 0
    for i in range(2,N-2):
        max_height = 0
        for j in range(i-2,i+3):
            if j == i:
                continue
            else:
                if max_height < building[j]:
                    max_height = building[j]
        if building[i] > max_height:
            result += building[i]-max_height

    print(f"#{test_case} {result}")
