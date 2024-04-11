#-*- encoding: utf-8 -*-
import os
import sympy
import re

while True:
    try:
        clear = lambda: os.system('cls')
        clear()
        print("Небольшие правила ввода:")
        print()
        print("Прописывать формулу полностью, т.е. прописывать все знаки (неправильно - 8x, правильно - 8*x, 2 * x1)")
        print("Скобки для уточнения порядка действия в спорных моментах лишними не будут")
        print("Переменные можно называть в удобном виде, но обязательно первая буква (неправильно - 1S, правильно - S0, ж1")
        print("Умножение - *, деление - /, возведение в степень - **, корень - sqrt()")
        print("Косинус - cos(), синус - sin(), тангенс - tan(), котангенс - cot()")
        print("Логарифм - log(16,4), 4 - основание, 16 - число")
        print("Дробь вводить с точкой")

        print()

        # Ввод формулы функции пользователем
        formula = input("Введите формулу функции: ")

        # Определение переменных
        variables = input("Введите переменные, разделенные пробелом: ").split()
        symbols = sympy.symbols(variables)
        delta_symbols = []

        delta = sympy.symbols('delta')

        for v in variables:
            delta_symbols.append(sympy.symbols('\u0394' + v))



        print("Систематическая погрешность:")

        # Вычисление частных производных
        derivatives = []
        for symbol in symbols:
            derivative = sympy.diff(formula, symbol)
            derivatives.append(derivative)

        delta_func = 0

        # Вывод результатов
        for i, symbol in enumerate(symbols):
            delta_func += abs(derivatives[i] * delta_symbols[i])


        # Приведение подобных слагаемых
        #delta_func = sympy.simplify(delta_func)

        # Применить метод pretty() для красивого вывода формулы
        delta_func_pretty = sympy.pretty(delta_func)
        '''delta_func_pretty = delta_func_pretty.replace('⋅', '·')
        delta_func_pretty = delta_func_pretty.replace('⎛', 'ſ')
        delta_func_pretty = delta_func_pretty.replace('⎝', 'ɭ')
        delta_func_pretty = delta_func_pretty.replace('⎞', 'ר')
        delta_func_pretty = delta_func_pretty.replace('⎠', 'Ј')'''

        delta_func_excel = str(delta_func)
        delta_func_excel = delta_func_excel.replace("**", "^")
        delta_func_excel = delta_func_excel.replace("sqrt", "КОРЕНЬ")
        delta_func_excel = re.sub(r"\d+\.\d+", lambda x: x.group().replace(".", ","), delta_func_excel)
        delta_func_excel = delta_func_excel.replace("cos", "COS")
        delta_func_excel = delta_func_excel.replace("sin", "SIN")
        delta_func_excel = delta_func_excel.replace("tan", "TAN")
        delta_func_excel = delta_func_excel.replace("cot", "COT")
        delta_func_excel = delta_func_excel.replace("asin", "ASIN")
        delta_func_excel = delta_func_excel.replace("acos", "ACOS")
        delta_func_excel = delta_func_excel.replace("acot", "ACOT")
        delta_func_excel = delta_func_excel.replace("atan", "ATAN")
        delta_func_excel = delta_func_excel.replace("ln", "LN")
        delta_func_excel = delta_func_excel.replace("log", "LOG")
        delta_func_excel = re.sub(r"log(\d+\.*\d, \d+\.*\d)", r"LOG(\1)", delta_func_excel)

        # Вывести формулу в красивом виде
        print()
        print("Результат:")
        print(delta_func)
        print()
        print("Результат в \"красивом\" виде:")
        print(delta_func_pretty)
        print()
        print("Результат для excel:")
        print(delta_func_excel)
        print()

        for v in variables:
            print("Введите ячейку в excel для " + '\u0394' + v)
            t = input()
            delta_func_excel = delta_func_excel.replace('\u0394' + v, t)

            print("Введите ячейку в excel для " + v)
            t = input()
            delta_func_excel = delta_func_excel.replace(v, t)

        print()
        print("Результат для excel с подстановкой:")
        print(delta_func_excel)



        print("Случайная погрешность:")

        # Вычисление частных производных
        derivatives = []
        for symbol in symbols:
            derivative = sympy.diff(formula, symbol)
            derivatives.append(derivative)

        delta_func = 0

        # Вывод результатов
        for i, symbol in enumerate(symbols):
            delta_func += (derivatives[i] * delta_symbols[i]) ** 2

        delta_func = sympy.sqrt(delta_func)

        # Приведение подобных слагаемых
        #delta_func = sympy.simplify(delta_func)

        # Применить метод pretty() для красивого вывода формулы
        delta_func_pretty = sympy.pretty(delta_func)
        '''delta_func_pretty = delta_func_pretty.replace('⋅', '·')
        delta_func_pretty = delta_func_pretty.replace('⎛', 'ſ')
        delta_func_pretty = delta_func_pretty.replace('⎝', 'ɭ')
        delta_func_pretty = delta_func_pretty.replace('⎞', 'ר')
        delta_func_pretty = delta_func_pretty.replace('⎠', 'Ј')'''

        delta_func_excel = str(delta_func)
        delta_func_excel = delta_func_excel.replace("**", "^")
        delta_func_excel = delta_func_excel.replace("sqrt", "КОРЕНЬ")
        delta_func_excel = re.sub(r"\d+\.\d+", lambda x: x.group().replace(".", ","), delta_func_excel)
        delta_func_excel = delta_func_excel.replace("cos", "COS")
        delta_func_excel = delta_func_excel.replace("sin", "SIN")
        delta_func_excel = delta_func_excel.replace("tan", "TAN")
        delta_func_excel = delta_func_excel.replace("cot", "COT")
        delta_func_excel = delta_func_excel.replace("asin", "ASIN")
        delta_func_excel = delta_func_excel.replace("acos", "ACOS")
        delta_func_excel = delta_func_excel.replace("acot", "ACOT")
        delta_func_excel = delta_func_excel.replace("atan", "ATAN")
        delta_func_excel = delta_func_excel.replace("ln", "LN")
        delta_func_excel = delta_func_excel.replace("log", "LOG")
        delta_func_excel = re.sub(r"log(\d+\.*\d, \d+\.*\d)", r"LOG(\1)", delta_func_excel)

        # Вывести формулу в красивом виде
        print()
        print("Результат:")
        print(delta_func)
        print()
        print("Результат в \"красивом\" виде:")
        print(delta_func_pretty)
        print()
        print("Результат для excel:")
        print(delta_func_excel)
        print()

        for v in variables:
            print("Введите ячейку в excel для " + '\u0394' + v)
            t = input()
            delta_func_excel = delta_func_excel.replace('\u0394' + v, t)

            print("Введите ячейку в excel для " + v)
            t = input()
            delta_func_excel = delta_func_excel.replace(v, t)

        print()
        print("Результат для excel с подстановкой:")
        print(delta_func_excel)
    

        print()
        print('''
            ./\…/\\
          (.‘•..•’.)
            ..=*=..
          (.\.||./.)~~** 
        ''')

        input()
    except Exception as e:
        print("Ошибка ввода")
        input()
