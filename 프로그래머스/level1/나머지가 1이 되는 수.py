def solution(n):
    answer = 0
    for i in range(n,0,-1):
        if n%i == 1:
            answer = i
    return answer

print(solution(10))

def solution2(n):
    for i in range(1,n):
        if n % i == 1:
            return i

print(solution2(10))