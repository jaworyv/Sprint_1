def digit_root(num):
    num = abs(num)

    while num >= 10:
        digits = []              # список цифр
        for d in str(num):       # перебираем символы строки
            digits.append(int(d))

        num = sum(digits)        # складываем цифры

    return num

print(digit_root(12)) 
