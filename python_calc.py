def calc(x, y, act):
    if act == '+':
        return x+y
    elif act == '-':
        return x-y
    elif act == '*':
        return x*y
    else:
        if y != 0:
            return round(x/y, 3)
        else:
            return "Деление на 0 невозможно"

while True:
    act = input("Выберите действие с числами: +, -, *, /: ")
    if act not in ('+', '-', '*', '/'):
        print("Введено некорректное действие")
        continue

    flag = False
    while not flag:
        try:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            flag = True
        except:
            print("Введено нечисловое значение")
            flag = False

    print(calc(x, y, act))
    print()

    stop = input("Будете еще производить расчеты? Да / Нет: ")
    if stop.lower() == 'да':
        continue
    else:
        break
    
