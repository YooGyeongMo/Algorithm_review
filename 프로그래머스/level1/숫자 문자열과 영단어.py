def solution(s):
    dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = ''
    word = ''
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            word += s[i]
            if word in dic:
                answer += str(dic[word])
                word = ''

    return int(answer)


def solution(s):
    dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
           'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = ''
    word = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            word += char
            if word in dic:
                answer += str(dic[word])
                word = ''

    return int(answer)