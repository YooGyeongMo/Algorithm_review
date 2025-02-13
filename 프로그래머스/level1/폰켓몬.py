def solution(nums):
    s = len(nums) // 2
    h_dict = set(nums)

    return min(len(h_dict), s)
