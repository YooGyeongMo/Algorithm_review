T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T+1):
    N = str(input())
    year = N[:4]
    month = N[4:6]
    day = N[6:]
    if year != "0000" and int(year) <= 9999:
        if month != "00" and 1 <= int(month) <= 12:
            if day != "00" and 1 <= int(day) <= days[int(month)-1]:
                print(f"#{test_case} {year}/{month}/{day}")
            else:
                print(f"#{test_case} -1")
        else:
            print(f"#{test_case} -1")
    else:
        print(f"#{test_case} -1")