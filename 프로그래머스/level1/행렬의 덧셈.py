def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[0])):
            row += [arr1[i][j] + arr2[i][j]]
        answer += [row]
    return answer


def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

def solution(arr1, arr2):
    return [[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]