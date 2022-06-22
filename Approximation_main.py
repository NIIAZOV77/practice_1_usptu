import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from math import log, exp
def approximation():
    # Функция для ввода данных
    def inputting(x):
        print('Введите значения', x, 'по одному, для завершения ввода чисел введите комманду "end"')
        List = []
        while True:
            I = input()
            if I == 'end':
                break
            else:
                List.append(float(I))

        return List
    # Фукция для возведения всех элементов массива в квадрат
    def square(list):
        return [i ** 2 for i in list]
    # Функция для перемножения элементов массивов
    def multiply(list1, list2):
        return [(list1[i] * list2[i]) for i in range(len(list1))]
    # Функция вычисления параметров a и b методом системы уравнений
    def calculate(a,b):
        ans = solve(a, b)
        return ans
    # Функция вычисления разности квадратов - фи
    def cost_func(a, b, list1, list2, ind):
        costSum = 0
        for i in range(len(list1)):
            if ind == 0:
                try:
                    theoY = a + b * xList[i]
                except:
                    theoY = 1000
            if ind == 1:
                try:
                    theoY = a * xList[i]**b
                except:
                    theoY = 1000
            if ind == 2:
                try:
                    theoY = a*exp(b*xList[i])
                except:
                    theoY = 1000
            if ind == 3:
                try:
                    theoY = a + b/xList[i]
                except:
                    theoY = 1000
            if ind == 4:
                try:
                    theoY = 1/(a + b*xList[i])
                except:
                    theoY = 1000
            if ind == 5:
                try:
                    theoY = xList[i]/(a + b*xList[i])
                except:
                    theoY = 1000
            if ind == 6:
                try:
                    theoY = a + b * log(xList[i])
                except: theoY = 1000
            cost = (theoY - list2[i])**2
            costSum += cost
        return costSum
    # Функия отображения графика
    def showing(a, b, xList, yList, answer):
        indPhi = int(indOfphi(a, b, xList, yList))

        show = input('Для отображения графика ведите "да"\n')
        if show == 'да':
            x = list(np.arange(-10, 10, 0.1))
            if indPhi == 0:
                y = [a + b * val for val in x]
                plt.plot(x, y)
            elif indPhi == 1:
                y = [a * val**b for val in x]
                plt.plot(x, y)
            elif indPhi == 2:
                y = [a*exp(b*val) for val in x]
                plt.plot(x, y)
            elif indPhi == 3:
                def func(val):
                    return a + b/val
                y = []
                for val in x:
                    if val == 0:
                        continue
                    else:
                        y.append(func(val))
                plt.plot(x, y)
            elif indPhi == 4:
                y = []
                for val in x:
                    if a + b*val == 0:
                        continue
                    else:
                        y1 = 1/([a + b*val])
                        y.append(y1)
                plt.plot(x, y)
            elif indPhi == 5:
                y = []
                for val in x:
                    if a + b * val == 0:
                        continue
                    else:
                        y1 = val / ([a + b * val])
                        y.append(y1)
                plt.plot(x, y)
            elif indPhi == 6:
                y = []
                for val in x:
                    if val <= 0:
                        continue
                    else:
                        y1 = a + b * log(val)
                        y.append(y1)
                plt.plot(x, y)
            plt.scatter(xList, yList)

            plt.show()
    # Функция создания списка из всех значений фи
    def listPhi(a, b, xList, yList):
        try:
            phi0 = float(cost_func(a, b, xList, yList, 0))
        except:
            phi0 = 1000
        try:
            phi1 = float(cost_func(a, b, xList, yList, 1))
        except:
            phi1 = 1000
        try:
            phi2 = float(cost_func(a, b, xList, yList, 2))
        except:
            phi2 = 1000
        try:
            phi3 = float(cost_func(a, b, xList, yList, 3))
        except:
            phi3 = 1000
        try:
            phi4 = float(cost_func(a, b, xList, yList, 4))
        except:
            phi4 = 1000
        try:
            phi5 = float(cost_func(a, b, xList, yList, 5))
        except:
            phi5 = 1000
        try:
            phi6 = float(cost_func(a, b, xList, yList, 6))
        except:
            phi6 = 1000
        phiL= [phi0, phi1, phi2, phi3, phi4, phi5, phi6]
        return phiL
    # Функция нахождения минимального значения фи из списка
    def indOfphi(a, b, xList, yList):
        list = listPhi(a, b, xList, yList)
        minimum = min(list)
        indPhi = list.index(minimum)
        return indPhi
    # Функия определения математической функции
    def typeOfFunc(xList, yList):
        indPhi = int(indOfphi(a, b, xList, yList))
        typeFunc = ''
        if indPhi == 0:
            typeFunc = 'y = a + b * x'
        elif indPhi == 1:
            typeFunc = 'y = a * x^b'
        elif indPhi == 2:
            typeFunc = 'y = a * e^(a * x)'
        elif indPhi == 3:
            typeFunc = 'y = a + b / x'
        elif indPhi == 4:
            typeFunc = 'y = 1 / (a + b * x)'
        elif indPhi == 5:
            typeFunc = 'y = x / (a+b*x)'
        elif indPhi == 6:
            typeFunc = 'y = a + b * ln(x)'
        return typeFunc

    xList = inputting('x')
    yList = inputting('y')
    A1 = sum(xList)
    A2 = sum(square(xList))
    B1 = sum(yList)
    B2 = sum(multiply(xList, yList))

    matrix = np.array([[len(xList), A1], [A1, A2]])
    vector = np.array([B1, B2]).reshape((2,1))

    answer = calculate(matrix, vector)
    a = float(answer[0])
    b = float(answer[1])

    print('Значения на подобии "-1.14535155e-15" - стремятся к нулю, на подобии "1.00000000e+00" - равняются числу которое стоит в целой части')
    print('Коэффициенты функции: ', 'a = ',  a, 'b = ', b)
    print('Расхождение теоритического значения с реальным состовляет - ', cost_func(a, b, xList, yList, indOfphi(a, b, xList, yList)) )
    print('Тип функции - ', typeOfFunc(xList, yList))

    #print(listPhi(a, b, xList, yList))
    # print(indOfphi(a,b, xList, yList))

    showing(a, b, xList, yList, answer)
approximation()