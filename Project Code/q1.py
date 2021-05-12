import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np

iterations = 1000

########################################################################
# 1.1


def p1():

    n = int(input("Input n: "))
    p = float(input("Input p: "))

    data = [0 for i in range(iterations)]

    for i in range(iterations):

        position = 0

        for j in range(n):

            if np.random.random() <= p:
                position += 1
            else:
                position -= 1

        data[i] = position

    q25, q75 = np.percentile(data, [.25, .75])
    bin_width = abs(2*(q75 - q25)*len(data)**(-1/3))

    if bin_width == 0.0:
        bin_width = 0.1

    bins = abs(round((max(data) - min(data))/bin_width))

    plt.hist(data, density=True, bins=bins//10)

    plt.xlabel('Final Position')

    plt.show()

########################################################################
# 1.2


def p2():

    n = int(input("Input n: "))
    p = float(input("Input p: "))

    data = [0 for i in range(iterations)]

    for i in range(iterations):

        position = 0

        for j in range(n):

            if np.random.random() <= p:
                position += 1
            elif position > 0:
                position -= 1

        data[i] = position

    q25, q75 = np.percentile(data, [.25, .75])
    bin_width = abs(2*(q75 - q25)*len(data)**(-1/3))

    if bin_width == 0.0:
        bin_width = 0.5

    bins = abs(round((max(data) - min(data))/bin_width))

    plt.hist(data, density=True, bins=bins)

    plt.xlabel('Final Position')

    plt.show()

########################################################################
# 1.3


def p3():

    object1 = int(input("The starting point of object 1 is: "))
    object2 = int(input("The starting point of object 2 is: "))

    p1 = float(input("The probability of object 1 moving right: "))
    p2 = float(input("The probability of object 2 moving right: "))

    data = [0 for i in range(iterations)]

    for i in range(iterations):

        stepstaken = 0

        ob1move = object1
        ob2move = object2

        while ob1move != ob2move:

            if np.random.random() <= p1:
                ob1move += 1
            else:
                ob1move -= 1

            if np.random.random() <= p2:
                ob2move += 1
            else:
                ob2move -= 1

            stepstaken += 1

        data[i] = stepstaken

    # data.sort()
    # ind = (np.array(data) > 500).tolist().index(1)
    # data = data[ind:]

    q25, q75 = np.percentile(data, [.25, .75])
    bin_width = abs(2*(q75 - q25)*len(data)**(-1/3))

    if bin_width == 0.0:
        bin_width = 0.1

    bins = round(float((max(data) - min(data)))/float(bin_width))

    if bins == 0:
        bins = 0.1

    plt.hist(data, density=True, bins=bins)

    plt.xlabel('Total Steps taken to meet')

    plt.show()

########################################################################
# Question 1


p1()
p2()
p3()
