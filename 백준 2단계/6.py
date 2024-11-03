# Take inputs for hours and minutes
a, b = map(int, input("").split())

# Take input for time to add in minutes
time = int(input(""))

# Add the minutes to the current minutes
b += time

# Check if minutes exceed 59
if b >= 60:
    # Calculate extra hours and adjust minutes
    a += b // 60
    b = b % 60 # 60보다 크면 나머지만큼 나오고 작으면 딱 그대로 나머지가 나오기때문이다.

# Check if hours exceed 23
if a >= 24:
    a = a % 24 # 24로 해서 딱 맞으면 0이 될것이고 그 위는 그만큼 남는 시간이 될것이고 작은 시간은 그대로 나올것이다.

# Print the new time
print(f"{a} {b}")