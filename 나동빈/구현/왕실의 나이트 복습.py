N = input()
x = (ord(N[0]) - ord('a')) + 1  # 'a' == 97 , 'A' == 65
y = int(N[1])

knight_steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for step in knight_steps:
    nx = x + step[0]
    ny = y + step[1]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        result += 1

print(result)