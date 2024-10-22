T = int(input())

for test_case in range(T):
    a = list(map(int,input().split()))
    sum = 0
    for num in a:
        sum += num
        aver = round(sum/len(a))
    print(f"#{test_case+1} {aver}")
