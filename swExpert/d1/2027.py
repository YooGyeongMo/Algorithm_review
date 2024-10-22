T = int(input())

for test_case in range(T):
    a = list(map(int,input().split()))
    sum = 0
    for num in a:
        if(num%2==1):
            sum += num
    print(f"#{test_case+1} {sum}")