# 파이썬 자료형은 기본 자료형 뿐만 아니라 사전 자료형, 집합 자료형 있어서 사용.

# 수 자료형
# 정수형은 많이 나오나 실수형은 빈도가 낮지만 정확히 다루자. 사칙연산시에 어떻게 되는지 파악.

# 정수형

a = 1000
print(a)
print(type(a))

# Hashmap 사용 없이도 파이썬은 사전 자료형 기능 사용가능.

a = 5.
# 생략 가능
print(a)

#10억의 지수 표현
a = 1e9 #유효 숫자 * 10의 지수
print(a) #출력 실수

a = 753.3e1
print(a) #출력 실수 7533.0

a = 3954e-3
print(a) #왼쪽으로 .3칸 이동 3.954

a = 0.3 + 0.6
print(a) # 부동소수점 방식을 이용 위는 0.9가 아닌 0.8999999... 가 나온다. 2진수 체계에서는 정확히 계산이 안되기 때문이다. round()함수이용하자.

print(round(a,4)) # 첫번째인자는 실수, 두번째 인자는 소수 몇번째자리까지 나타낼것인지.

a = 7
b = 5

print(a/b) # 실수형
print(a%b) # 나머지
print(a//b) # 몫
print(a**b) #거듭제곱 a^b를 의미

#리스트 자료형

# 빈리스트 선언

a = []

b = list()

#1차원 리스트 초기화

n = 10
a = [0] * n
print(a)

# 리스트 요소값 슬라이싱 변경

a[3] = 7
print(a)
print(a[0:4]) #슬라이싱

# 리스트 컴프리헨션

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2 == 0]
print(array)

#컴프리헨션 사용 안 할 시에.
a = []
for i in range(20):
    if i % 2== 0:
        a.append(i)
print(array)

array = [i*i for i in range(1,10)]
print(array)

# 컴프리헨션 2차원 배열
# N X M 행렬

n = 3
m = 4
array =[[0]*m for _ in range(n)]

print(array)

#입력과 동시에 선언
# array = [list(map(int,input().split())) for _ in range(n)]
#
# print(array)
#
# # 한 리스트 씩
# arr = []
#
# for i in range(n):
#     arr.append(list(map(int, input().split())))
# print(arr)

a = [1, 4, 3]

a.append(2) #뒤에 들어감
print(a) # O(1)

#오름차순 정렬
a.sort() # O(NlogN)
print(a)

#내림차순 정렬
a.sort(reverse = True)
print(a)

#리스트 원소 뒤집기
a.reverse()
print(a)

# 특정 인덱스에 데이터 추가

a.insert(2,5) # 그 자리에 있는 데이터는 뒤로 물러남
print(a)

# 특정 값 세아리기

print(a.count(3))
b = a.count(3)
print(b)

# 특정 값 삭제하기. 하나만 삭제됨
a.remove(1)
print(a)

# reverse, remove, count, insert 다 O(N)

a = [1, 2, 3, 3, 4, 5, 5, 5, 5]
a.remove(3) # remove 사용시 하나만 삭제됨
print(a)

remove_set = {3, 5}

result = [i for i in a if i not in remove_set]

print(result)