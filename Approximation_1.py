def approximation():
        import numpy as np
        import matplotlib.pyplot as plt
        from scipy.linalg import solve
        from math import log, exp, inf
        try:
            # Функция для ввода данных
            def inputting():
                adress = input('Введите адрес файла (без кавычек)\n')
                file = open(adress, 'r')
                file1 = file.read().split('\n')
                list = []
                for row in file1:
                    num = float(row)
                    list.append(num)
                file.close()

                return list
            # Функция для возведения в квадрат всех чисел списка
            def square(list):
                        return [i ** 2 for i in list]
            # Функция для перемножения всех членов двух списков
            def multiply(list1, list2):
                return [(list1[i] * list2[i]) for i in range(len(list1))]
            # Функция для вычисления коэффициентов
            def calculate(xList, yList):
                try:
                    A1 = sum(xList)
                    A2 = sum(square(xList))
                    B1 = sum(yList)
                    B2 = sum(multiply(xList, yList))
                    matrix = np.array([[len(xList), A1], [A1, A2]])
                    vector = np.array([B1, B2]).reshape((2, 1))
                    ans = solve(matrix, vector)
                    return ans
                except:
                    ans = [inf, inf]
                    return ans
            # Функция дя логарифмирования всех элементов списка
            def logar(list):
                try:
                    l = []
                    for i in list:
                        l.append(log(i))
                    return l
                except:
                    l = []
                    for i in list:
                        l.append(inf)
                    return l
            # Функция для деления 1 на каждый элемент списка
            def division(list):
                try:
                    l = []
                    for i in list:
                        l.append(1/i)
                    return l
                except:
                    l = []
                    for i in list:
                        l.append(inf)
                    return l
            # Функция для деления элементов одного списка на элементы другого
            def list_division(xlist, ylist):
                try:
                    l = []
                    for i in range(len(xlist)):
                        l.append(xlist[i]/ylist[i])
                    return l
                except:
                    l = []
                    for i in (xlist):
                        l.append(inf)
                    return l
            # Функция для вычисления функции затрат - Фи
            def cost_func(a, b, list1, list2, ind):
                costSum = 0
                for i in range(len(list1)):
                    if ind == 0:
                            theoY = a[0] + b[0] * list1[i]
                    if ind == 1:
                        try:
                            theoY = a[1] * (list1[i]) ** b[1]
                            float(theoY)
                        except:
                            return None
                    if ind == 2:
                        try:
                            theoY = a[2] * exp(b[2] * list1[i])
                            float(theoY)
                        except:
                            return None
                    if ind == 3:
                        try:
                            theoY = a[3] + b[3] / list1[i]
                        except:
                            return None
                    if ind == 4:
                        try:
                            theoY = 1 / (a[4] + b[4] * list1[i])
                        except:
                            return None
                    if ind == 5:
                        try:
                            theoY = list1[i] / (a[5] + b[5] * list1[i])
                        except:
                            return None
                    if ind == 6:
                        try:
                            theoY = a[6] + b[6] * log(list1[i])
                            float(theoY)
                        except:
                            return None
                    cost = (((theoY) - list2[i]) ** 2)
                    costSum += cost
                return costSum
            # Функция для составления списка из всех элементов Фи
            def listPhi(a, b, xList, yList):
                    if cost_func(a, b, xList, yList, 0) != None:
                        phi0 = float(cost_func(a, b, xList, yList, 0))
                    else:
                        phi0 = inf
                    if cost_func(a, b, xList, yList, 1) != None:
                        phi1 = float(cost_func(a, b, xList, yList, 1))
                    else:
                        phi1 = inf
                    if cost_func(a, b, xList, yList, 2) != None:
                        phi2 = float(cost_func(a, b, xList, yList, 2))
                    else:
                        phi2 = inf
                    if cost_func(a, b, xList, yList, 3) != None:
                        phi3 = float(cost_func(a, b, xList, yList, 3))
                    else:
                        phi3 = inf
                    if cost_func(a, b, xList, yList, 4) != None:
                        phi4 = float(cost_func(a, b, xList, yList, 4))
                    else:
                        phi4 = inf
                    if cost_func(a, b, xList, yList, 5) != None:
                        phi5 = float(cost_func(a, b, xList, yList, 5))
                    else:
                        phi5 = inf
                    if cost_func(a, b, xList, yList, 6) != None:
                        phi6 = float(cost_func(a, b, xList, yList, 6))
                    else:
                        phi6 = inf
                    phiL = [phi0, phi1, phi2, phi3, phi4, phi5, phi6]
                    return phiL
            # Функция для нахождения коэффициента наименьшего Фи
            def indOfphi(a, b, xList, yList):
                list = listPhi(a, b, xList, yList)
                minimum = min(list)
                indPhi = list.index(minimum)
                return indPhi
            # Функция для определения типа математической функции
            def typeOfFunc(a, b, xList, yList):
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
                    typeFunc = 'y = x / (a + b * x)'
                elif indPhi == 6:
                    typeFunc = 'y = a + b * ln(x)'
                return typeFunc
            # Функция для отображения графика
            def showing(a, b, xList, yList):
                indPhi = int(indOfphi(a, b, xList, yList))

                show = input('Для отображения графика ведите "да"\n')
                if show == 'да':
                    minimum = min(xList) - (min(xList) / 10)
                    maximum = max(xList) + (max(xList) / 10)
                    x = list(np.arange(minimum, maximum, 0.01))
                    if indPhi == 0:
                        y = [[a0] + b[0] * val for val in x]
                        a = round(a[0], 4)
                        b = round(b[0], 4)
                        text = 'y = ' + str(a)+ '+' + str(b) + ' * x'
                        plt.title(text)

                        plt.plot(x, y)
                    elif indPhi == 1:
                        y = [a[1] * val ** b[1] for val in x]
                        a = round(a[1], 4)
                        b = round(b[1], 4)
                        text = 'y = ' + str(a) + ' * x^' + str(b)
                        plt.title(text)
                        plt.plot(x, y)
                    elif indPhi == 2:
                        y = [a[2] * exp(b[2] * val) for val in x]
                        a = round(a[2], 4)
                        b = round(b[2], 4)
                        text = 'y = ' + str(a) + ' * e^' + str(b) + '* x'
                        plt.title(text)
                        plt.plot(x, y)
                    elif indPhi == 3:
                        y = [a[3] + b[3] / val for val in x]
                        a = round(a[3], 4)
                        b = round(b[3], 4)
                        text = 'y = ' + str(a) + '+' + str(b) + ' / x'
                        plt.title(text)
                        plt.plot(x, y)
                    elif indPhi == 4:
                        y =[1 / (a[4] + b[4] * val) for val in x]
                        a = round(a[4], 4)
                        b = round(b[4], 4)
                        text = 'y = 1 / (' + str(a) + str(b)+' * x)'
                        plt.title(text)
                        plt.plot(x, y)
                    elif indPhi == 5:
                        y = [val / (a[5] + b[5] * val) for val in x]
                        a = round(a[5], 4)
                        b = round(b[5], 4)
                        text = 'y = x / (' + str(a)+ ' + ' + str(b) + ' * x)'
                        plt.title(text)
                        plt.plot(x, y)
                    elif indPhi == 6:
                        y = [a[6] + b[6] * log(val) for val in x]
                        a = round(a[6], 4)
                        b = round(b[6], 4)
                        text = 'y = ' + str(a)+ '+' + str(b) + ' * ln(x)'
                        plt.title(text)
                        plt.plot(x, y)
                    plt.xlabel('x')
                    plt.ylabel('y')
                    plt.scatter(xList, yList)

                    plt.show()

            # Списки со значениями методом примененным в Approximation_2
            # text = input('Enter a file adress (without quotes) \n')
            # data = np.genfromtxt(str(text), delimiter=',', dtype=np.float64)
            # data = data.transpose()
            # xList_t = list(data[:1])
            # yList_t = list(data[1:])
            # theox = list(np.transpose(xList_t))
            # theoy = list(np.transpose(yList_t))
            # xList_0 = []
            # yList_0 = []
            # for i in theox:
            #     xList_0.append(float(i))
            # for i in theoy:
            #     yList_0.append(float(i))
            xList_0 = inputting()
            yList_0 = inputting()
            xList_1 = logar(xList_0)
            yList_1 = logar(yList_0)
            xList_2 = xList_0
            yList_2 = yList_1
            xList_3 = division(xList_0)
            yList_3 = yList_0
            xList_4 = xList_0
            yList_4 = division(yList_0)
            xList_5 = xList_0
            yList_5 = list_division(xList_0, yList_0)
            xList_6 = xList_1
            yList_6 = yList_0

            answer_0 = calculate(xList_0, yList_0)
            answer_1 = calculate(xList_1, yList_1)
            answer_2 = calculate(xList_2, yList_2)
            answer_3 = calculate(xList_3, yList_3)
            answer_4 = calculate(xList_4, yList_4)
            answer_5 = calculate(xList_5, yList_5)
            answer_6 = calculate(xList_6, yList_6)

            a0  = float(answer_0[0])
            a1  = exp(float(answer_1[0]))
            a2  = exp(float(answer_2[0]))
            a3  = float(answer_3[0])
            a4  = float(answer_4[0])
            a5  = float(answer_5[0])
            a6  = float(answer_6[0])
            b0 = float(answer_0[1])
            b1 = float(answer_1[1])
            b2 = float(answer_2[1])
            b3 = float(answer_3[1])
            b4 = float(answer_4[1])
            b5 = float(answer_5[1])
            b6 = float(answer_6[1])

            a = [a0, a1, a2, a3, a4, a5, a6]
            b = [b0, b1, b2, b3, b4, b5, b6]

            print('Коэффициенты функции: ', 'a = ',  a[indOfphi(a, b, xList_0, yList_0)], 'b = ', b[indOfphi(a, b, xList_0, yList_0)])
            print('Расхождение теоритического значения с реальным состовляет - ', cost_func(a, b, xList_0, yList_0, indOfphi(a, b, xList_0, yList_0)))
            print('Тип функции - ', typeOfFunc(a, b, xList_0, yList_0))
            print(cost_func([-3.63029144], [1.16636235], xList_0, yList_0, 0))
            showing(a, b, xList_0, yList_0)

        except:
            print('Неверный формат данных')
            quit()
approximation()