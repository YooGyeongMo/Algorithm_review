def solution(t, p):
    check = ''
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        check = t[i:i+len(p)]
        if int(check) <= int(p):
            answer += 1
    return answer