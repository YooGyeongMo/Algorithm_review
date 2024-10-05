a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b)
print(c)


'''
참고
3개의 요소로 이루어지는 3항 연산은
"x if C else y" 의 형태로 작성이 된다.
- C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
- x : C의 평가 결과가 True 일 때 사용할 값
- y : C의 평가 결과가 True 가 아닐 때 사용할 값
'''