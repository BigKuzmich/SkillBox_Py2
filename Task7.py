print("Задача 7. Режем число на части")

num = int(input("Введите 4х значное число: "))
if 1000 <= num <= 9999:
    a = num // 1000
    b = num // 100 % 10
    c = num % 100 // 10
    d = num % 10
    print(a)
    print(b)
    print(c)
    print(d)
elif num > 9999:
    print("Ваше число велико для меня!")
elif num < 1000:
    print("Ваше число слишком мало для меня")

