def solution(s, n):
    answer = []
    for i in s:
        if i.isupper():
            answer.append(chr((ord(i) - 65 + n) % 26 + 65))
        elif i.islower():
            answer.append(chr((ord(i) - 97 + n) % 26 + 97))
        else:
            answer.append(' ')

    return ''.join(answer)

# 다른 풀이

def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif i >= 'a' and i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer