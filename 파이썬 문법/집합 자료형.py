# 집합 처리하기 위해서 집합 자료형

# 특징
# 중복을 허용 X
# 순서가 없음
# O(1)

# 특정 데이터가 있는지 중복 체크할 때 용이
data = set([1, 2, 3, 4, 5, 5])

print(data)

data = {1, 2, 3, 3, 3, 3, 3, 3}
print(data)


#합집합,교집합,차집합

a = {1, 2, 3 ,4, 5}
b = {1, 2, 5, 6, 7}
print(a|b) #합집합
print(a&b) #교집합
print(a-b)#차집합

# O(1) 가지는 집합 함수

a.add(7)
print(a)

a.update([8,9,10,11])
print(a)

a.remove(3)
print(a)