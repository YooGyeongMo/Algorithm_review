N = input()

# .isdigit()
# .isalpha()

result = []
value = 0

for char in N:
    if char.isdigit():
        value += int(char)
    else:
        result.append(char)

result.sort()
if value != 0:
    result.append(str(value))

print("".join(result))