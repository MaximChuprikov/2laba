while True:
    try:
        a = int(input())
        b = a
        break
    except ValueError:
        print('Должно быть введено число!')

if a <= 0:
    print("FALSE")
elif a == 1:
    print("TRUE")
else:
    while a>0 and a%4 == 0:
        a = a//4
        if a == 1:
            print("TRUE")
    if a != 1:
            print("FALSE")

if b != 1:
    for i in range(2, 10):
        j=1
        while j <= b:
            if j == b:
                print("Число является степенью цифры:", i)
                break
            else:
                j*=i
else:
    print("Число является степенью любой цифры")