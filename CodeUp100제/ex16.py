a, b = map(int, input().split())
c = a+b
print(c)

a, b = input().split()
c = int(a) + int(b)
print(c)

'''
	1.	input().split(): 사용자 입력을 공백을 기준으로 나누어 리스트로 반환합니다.
	•	예를 들어, 입력이 3 4인 경우 ["3", "4"]가 됩니다.
	2.	map(int, input().split()): 입력받은 문자열을 int로 변환합니다.
	•	예를 들어, ["3", "4"]는 [3, 4]로 변환됩니다.
	3.	a, b = map(int, input().split()): 각각의 값을 a와 b에 저장합니다.
	•	a = 3, b = 4로 저장됩니다.
	4.	c = a + b: 두 정수를 더한 값을 c에 저장합니다.
	5.	print(c): 더한 결과를 출력합니다.

'''