def solution(sizes):
    width = []
    height = []

    for i in sizes:
        width.append(max(i[0], i[1]))
        height.append(min(i[0], i[1]))

    answer = max(width) * max(height)

    return answer


def solution(sizes):
    width = []
    height = []

    for i in sizes:
        # width.append(max(i[0],i[1]))
        # height.append(min(i[0],i[1]))
        width.append(max(i))
        height.append(min(i))

    answer = max(width) * max(height)

    return answer


# 직사각형 돌릴때 결국 넓이임,
# 두 수 중에서 큰거를 앞으로 당기고, 작은 것을 뒤로 정렬한 후
# 그중에서 가장 큰것들로 하면 최소 직사각형이 된다.


def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
