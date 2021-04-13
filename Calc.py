import re

def Calculate():
    try:
        value = int(input("Введите первое число: ")) # Если ввести не число, метод завершается
    except:
        print("Вы ввели не число")
        return
    print("Введите операцию и следующее число (прим. +2) или '=' чтобы вывести результат ")
    print("Возможные операции: + сложить, - вычесть, * умножить, / разделить, ^ возвести в степень")
    work = True
    while (work):
        currentValue = input(">> ")
        if len(currentValue) < 1: # Проверяем есть ли символы в строке
            print("Неверный ввод")
            return
        operation = currentValue[0]
        currentValue = re.sub("[^0-9]", "", currentValue) # Удаляем все, кроме цифр
        if len(currentValue) >= 1: # Проверяем есть ли символы в строке после удаления, затем выбираем операцию
            if operation == '+':
                value += int(currentValue)
            elif operation == '-':
                value -= int(currentValue)
            elif operation == '*':
                value *= int(currentValue)
            elif operation == '/':
                value /= int(currentValue)
            elif operation == '^':
                value **= int(currentValue)
            else:
                print("Не могу выполнить эту операцию")
        else:
            if operation == '=':
                work = False
            else:
                print("Неверный ввод")
    return value

while(True):
    result = Calculate()
    print(result)