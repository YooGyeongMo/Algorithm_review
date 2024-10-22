T = int(input())

for test_case in range(1,T+1):
    a = list(map(int,input().split()))
    max = 0
    for j in range(10):
        if(a[j] > max):
            max = a[j]
    print(f"#{test_case} {max}")