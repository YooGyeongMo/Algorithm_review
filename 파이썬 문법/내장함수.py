# iterable 객체 반복 가능한 객체에서 쓸 수 있는 함수

result = sum([1, 2, 3, 4, 5])

print(result)

result = min(7, 5, 4, 2)
# result = min([6,5,42]) 리스트도 가능
print(result)

result = max(3,2,4,60)
print(result)

#eval 함수는 문자열 수식이 들어가면 계산
result = eval("(3+5)*5")
print(result)

result = sorted([9, 4, 5, 6, 2])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)

result = sorted([('홍길동', 35),('김길동', 40),('홍박사', 60)], key = lambda x: x[1]) # key는 요소임
print(result)


#sort()함수는 그 리스트 자체를 변경해서 리턴함.
