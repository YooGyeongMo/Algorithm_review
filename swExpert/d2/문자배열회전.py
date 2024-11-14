def rotate_90(arr):
    arrR = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrR[i][j] = arr[N-1-j][i]

    return arrR

def rotate_180(arr):
    arrR = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrR[i][j] = arr[N-1-i][N-1-j]

    return arrR

def rotate_270(arr):
    arrR = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrR[i][j] = arr[j][N-1-i]

    return arrR

T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    data_list = [list(map(int, input().split())) for i in range(N)]

    arr1 = rotate_90(data_list)
    arr2 = rotate_180(data_list)
    arr3 = rotate_270(data_list)

    print(f"#{test_case}")

    for a,b,c in zip(arr1,arr2,arr3):
        print("".join(map(str,a)),"".join(map(str,b)),"".join(map(str,c)))

    # for i in range(N):
    #     print("".join(map(str, arr1[i])),"".join(map(str, arr2[i])), "".join(map(str, arr3[i])))