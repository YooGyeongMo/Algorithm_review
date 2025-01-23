N = input()

row = int(N[1])
column = (int(ord(N[0])) - int(ord('a'))) +1

steps = [(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)