def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


def solution2(A,B):

    zipped_list = zip(sorted(A),sorted(B, reverse = True))
    answer = 0

    for a, b in zipped_list:
        answer += a*b

    return answer

print(solution2([1,4,2],[3,4,5]))