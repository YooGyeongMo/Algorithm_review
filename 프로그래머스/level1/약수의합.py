def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

def solution2(num):
    return num + sum([i for i in range(1,(num//2)+1) if num % i == 0])
# 약수는 num의 절반보다 큰 값일 수 없습니다(자기 자신 제외).
# 	•	예: 12의 약수 중 자기 자신을 제외한 약수는 1부터 6까지만 확인하면 됩니다.
# 	•	1, 2, 3, 4, 6 → 12 // 2 = 6까지 확인.
# 	•	따라서, 약수 계산을 효율적으로 하기 위해 **(num // 2) + 1**까지 반복합니다.