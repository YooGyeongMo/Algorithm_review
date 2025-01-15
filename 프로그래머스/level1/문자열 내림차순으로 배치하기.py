def solution(s):
    answer = ''
    upper = ''
    lower = ''

    a_list = list(s)

    a_list.sort(reverse=True)

    for i in a_list:
        if i.isupper():
            upper += i
        else:
            lower += i

    answer = lower + upper

    return answer

def solution(s):

    return ''.join(sorted(s,reverse=True))