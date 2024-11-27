import math

while True:
    print("Калькулятор:\n1) Складні операції\n2) Прості операції")
    choice1 = int(input("Оберіть операцію: "))
    if choice1 == 1:
        print("1) Знайти корінь\n2) Квадрат числа\n3) Піднести число до степення\n4) Знайти НОД\n5) Вийти\n")
        choice = int(input("Оберіть операцію: "))
        if choice == 5:
            break
        elif choice in (1, 2):
            num1 = int(input("Введіть число: "))
        else:
            num1 = int(input("Введіть перше число: "))
            num2 = int(input("Введіть друге число: "))
        if choice == 1:
            print(f"Корінь: {num1} = {math.sqrt(num1)}\n")
        elif choice == 2:
            print(f"Квадрат {num1} = {math.pow(num1, 2)}\n")
        elif choice == 3:
            print(f"Число {num1} у степені {num2} = {math.pow(num1, num2)}\n")
        elif choice == 4:
            print(f"Найбільший спільний дільник {num1} та {num2} = {math.gcd(num1, num2)}\n")
    else:
        print("1) Додавання\n2) Віднімання\n3) Множення\n4) Ділення\n5) Вийти\n")
        choice = int(input("Оберіть операцію: "))

        if choice == 5:
            break
        else:
            num1 = int(input("Введіть перше число: "))
            num2 = int(input("Введіть друге число: "))

            if choice == 1:
                print(f"{num1} + {num2} = {num1 + num2}\n")
            elif choice == 2:
                print(f"{num1} - {num2} = {num1 - num2}\n")
            elif choice == 3:
                print(f"{num1} * {num2} = {num1 * num2}\n")
            elif choice == 4:
                if num2 == 0:
                    print("Не можна ділити на 0\n")
                else:
                    print(f"{num1} / {num2} = {num1 / num2}\n")

