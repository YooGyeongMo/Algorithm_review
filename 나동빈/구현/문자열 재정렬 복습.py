S = input()

word = []
digit = 0
for char in S:
    if char.isalpha():
        word.append(char)
    else:
        digit += int(char)

word.sort()

if digit > 0 :
    word.append(str(digit))

print(''.join(word))