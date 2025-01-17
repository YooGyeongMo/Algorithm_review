def solution(s):
    arr = list(map(str, s.split(' ')))
    answer = []

    for word in arr:
        new_word = ''
        for j in range(len(word)):
            if j % 2 == 0:
                new_word += word[j].upper()
            else:
                new_word += word[j].lower()
        answer.append(new_word)

    return ' '.join(answer)

# 문제의 키 포인트는 s.split()을 하면 문자의 공백을 기준으로 나눈다
# 하지만 문제에서는 하나이상의 연속된 공백이 존재한다고 한다.
# 그래서 문자 사이에 기본적으로 ' ' 하나의 공백과 그 이상의 공백을 ' ' 하나하나 리스트에 담고, 구별해주고 합쳐줘야한다.

# 입력: "try   hello    world" try 와 hello 사이 공백 3번, hello와 world 사이 공백 4번
# 1.split(' ')으로 처리:
# arr = s.split(' ')하면 ' '이니까 한번은
# 결과: ['try', '', '', 'hello', '', '', '', 'world']
# ' '.join() 하면 요소 사이에 ' '가 붙어서 합칠때 공백이 유지된다.


s = 'try  hello  world'

arr = s.split(' ')
print(arr)
print(' '.join(arr))