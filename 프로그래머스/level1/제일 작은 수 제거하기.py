def solution(arr):
    if len(arr) == 1:
        arr[0] = -1
        return arr
    else:
        arr.remove(min(arr))

    return arr