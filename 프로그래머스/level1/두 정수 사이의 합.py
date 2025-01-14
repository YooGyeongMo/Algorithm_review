def solution(a, b):
    answer = 0
    max_value = max(a,b)
    min_value = min(a,b)
    for i in range(min_value,max_value+1):
        answer += i
    return answer

#  다른 풀이

def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))