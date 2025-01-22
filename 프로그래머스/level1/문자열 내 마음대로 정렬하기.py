def solution(strings, n):
    answer = []

    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()

    for i in strings:
        answer.append(i[1:])

    return answer



def solution(strings, n):
    answer = []
    for i in strings :
        answer.append(i[n]+i)
    answer.sort()
    return [i[1:] for i in answer]

def solution(strings, n):
    return sorted(strings, key = lambda x : (x[n],x))


# sort, sorted에 key인자를 넣어줌으로써 정렬 기준을 정할 수 있다.
# key 기준으로 정렬을 할 경우 오직 key 기준으로만 정렬을 한다. key이외의 나머지 요소에 대해선 정렬되지 않음.
# lambda를 이용한 key 설정에서 튜플을 넣어줌으로써 정렬의 우선순위를 지정할 수 있다.

c = sorted(a, key = lambda x : x[0])

# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

d = sorted(a, key = lambda x : x[1])

# d = [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]


# ▷ 비교할 아이템이 요소가 복수 개일 경우, 튜플로 우선순위를 정해줄 수 있다.

# ▷ -를 붙이면, 현재와 반대차순으로 정렬된다.

e = sorted(a, key = lambda x : (x[0], -x[1]))
# => [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]

f = sorted(a, key = lambda x : -x[0])
# => [(5, 1), (5, 2), (3, 0), (1, 2), (0, 1)])


s = ['2 A', '1 B', '4 C', '1 A']
# s.sorted(s, key=lambda x: (x.split()[1], x.split()[0]))
# => ['1 A', '2 A', '1 B', '4 C']


 # list(map(lambda x: x , list ) 표현식

list(map(lambda x: x+10, [1,2,3]))

# => [11, 12, 13]


# 4. filter()
#  조건식의 boolean 값이 True 참인 요소만 반환한다.
#
a = [8, 4, 2, 5, 2, 7, 9, 11, 26, 13]
#
result = list(filter(lambda x : x > 7 and x < 15, a))
#
# => [8, 9, 11, 13]

# sort
# 리스트.sort(key = <function>, reverse = <bool>)
# 리스트 원본을 정렬된 상태로 변경함

# sorted
# sorted(iterable, key = <function> , reverse = <bool>)
# 원본을 변형시키지 않고 정렬된 결과를 리턴함
# 리스트 뿐만 아니라 iterable 자료형에 사용 가능

# reverse, key 매개변수
# reverse= 로 내림차순True 또는 오름차순False 변경 가능
# key= 값을 기준으로 정렬 가능


#문자열의 개수를 기준으로 정렬
list_str = ['hi', 'this', 'hello', 'python']
print(sorted(list_str, key=lambda x: len(x)))


#특정 문자(x[n])을 기준으로 정렬
print(sorted(list_str, key=lambda x: x[n]))


#2차원 리스트 중 한 요소 기준으로 정렬
list_num = [[1, '가'], [3, '다'], [4, '라'], [2, '나']]
print(sorted(list_num, key=lambda x: x[0]
