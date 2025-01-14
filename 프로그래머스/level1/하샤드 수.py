def solution(x):
    a_list = list(map(int, str(x)))

    if x % sum(a_list) == 0:
        return True
    else:
        return False


# 다른 풀이

def Harshad(n):
    return n%sum(int(x) for x in str(n)) == 0
