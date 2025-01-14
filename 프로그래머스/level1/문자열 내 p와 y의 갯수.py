def solution(s):
    answer = True
    p_c = s.lower().count('p')
    y_c = s.lower().count('y')

    if p_c == y_c:
        return answer
    elif p_c == 0 and y_c == 0:
        return answer
    else:
        return False

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
