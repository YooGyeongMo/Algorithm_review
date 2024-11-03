N, M = map(int,input().split())

array = map(int,input().split())

def binary_search(array, target, start, end):
    mid = (start + end) // 2
    total = 0

    if start > end:
        if total > target:
            return mid
        else:
            return None

    for i in array:
        if i > mid:
            total += i - mid
    if total > target:
        return binary_search(array,target,mid+1,end)
    elif total < target:
        return binary_search(array,target,start, mid-1)
    else:
        return mid

result = binary_search(array,M, 0, max(array))

print(result)