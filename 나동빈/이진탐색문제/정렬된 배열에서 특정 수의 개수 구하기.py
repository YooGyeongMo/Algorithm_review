from bisect import bisect_left, bisect_right

N,x = map(int,input().split())
array = list(map(int,input().split()))

def func(array, x):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)
    result = right_index - left_index

    return result

result = func(array,x)

if result == 0:
    print(-1)
else:
    print(result)