n = int(input())
nums = input().split()

for i in range(n):
    nums[i] = int(nums[i])

# print(reversed(nums)) // 객체 반환해서 list(), tuple() 같은 함수로 덮어야함.

nums.reverse() # list로 뱉으니까 이를 다시 하나의 정수로 뱉어야함.
print(nums)

# for i in range(-1,(-len(nums)-1),-1):
#     print(f"{nums[i]}", end = " ")

# for i in range(n-1, -1, -1) :