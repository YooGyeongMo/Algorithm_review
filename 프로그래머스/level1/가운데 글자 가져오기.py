def solution(s):
    answer = len(s) // 2

    if len(s) % 2 == 0:
        return s[answer - 1:answer + 1]
    else:
        return s[answer]