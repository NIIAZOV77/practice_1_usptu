import numpy as np
import matplotlib.pyplot as plt
from math import log, exp, inf


def inputting():
    text = input('Enter a file adress (without quotes) \n')
    data = np.genfromtxt(str(text), delimiter=',', dtype=np.float64)
    return data
def costFunction(x, y, theta):
    h_x = np.matmul(np.transpose(theta), x)
    S1 = (h_x - y) ** 2
    S = S1.sum()
    J = S / (2 * x1.shape[1])
    return J
def gradientDescent(x, y, theta):
    alpha = float(input('Enter an alpha: '))
    num_it = int(input('Enter a number of iterations: '))
    J_theo = inf
    for i in range(num_it):
        theta_t = theta
        theta = theta - alpha/x1.shape[1] * np.transpose(np.matmul((np.transpose(np.matmul(np.transpose(x), theta) - np.transpose(y))), np.transpose(x)))
        J_h = costFunction(x, y, theta)
        if J_h > J_theo:
            break
            return theta_t
        J_theo = J_h
    return theta
def showing(x1, y, theta):
    a = float(theta[0])
    b = float(theta[1])
    y1 = [a + b * val for val in x1]

    a = round(a, 4)
    b = round(b, 4)
    text = 'y = ' + str(a) + '+' + str(b) + ' * x'
    plt.title(text)

    plt.scatter(np.transpose(x1), np.transpose(y))
    plt.plot(np.transpose(x1), np.transpose(y1))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

data = inputting().transpose()
x1 = data[:1]
xList_0 = list(data[:1])
yList_0 = list(data[1:])
x0 = np.ones((1, x1.shape[1]))
x = np.concatenate((x0,x1),axis=0)
y = data[1:]
theta = np.array([[0], [0]])

theta = gradientDescent(x, y, theta)
print(theta)
J = costFunction(x, y, theta)
print(J)
showing(x1, y, theta)