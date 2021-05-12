import random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import math

iterations = 50000

########################################################################
# 4.1


def p1():

    data = []
    for i in range(iterations):

        angle1 = np.random.uniform(0, 2*math.pi)
        angle2 = np.random.uniform(0, 2*math.pi)

        data.append(2*radius*math.sin(abs((angle2-angle1)/2)))

    q25, q75 = np.percentile(data, [.25, .75])
    bin_width = abs(2*(q75 - q25)*len(data)**(-1/3))

    if bin_width == 0.0:
        bin_width = 0.1

    bins = round(float((max(data) - min(data)))/float(bin_width))

    if bins == 0:
        bins = 0.1

    plt.hist(data, weights=np.ones_like(data) / len(data), bins=bins//10)

    plt.show()

########################################################################
# 4.2


def p2():

    data = []

    inner = 0
    outer = 0

    for i in range(iterations):

        point = random.random()*radius

        data.append(2*math.sqrt((radius**2)-(point**2)))

        if (point < radius/2):
            inner += 1
        if (point < radius):
            outer += 1

    q25, q75 = np.percentile(data, [.25, .75])
    bin_width = 2*(q75 - q25)*len(data)**(-1/3)
    bins = round((max(data) - min(data))/bin_width)

    plt.hist(data, weights=np.ones_like(data) / len(data), bins=bins)

    plt.show()

    print("Outer circle points: ", outer, " Inner circle points: ", inner)

    print("Ratio of points: ", round(outer/inner, 2))

########################################################################
# 4.3


def p3():

    data = []
    inner = 0
    outer = 0

    for i in range(iterations):

        # point = np.sqrt(np.random.random()) * radius

        # data.append(2*math.sqrt((radius**2)-(point**2)))

        tempx = np.random.uniform(-radius, radius, 1)
        tempy = np.random.uniform(-radius, radius, 1)

        while (np.sqrt(tempx**2 + tempy**2) > radius):

            tempx = np.random.uniform(-radius, radius, 1)
            tempy = np.random.uniform(-radius, radius, 1)

        if (np.sqrt(tempx**2 + tempy**2) < radius/2):
            inner += 1
        if (np.sqrt(tempx**2 + tempy**2) < radius):
            outer += 1

        point = math.sqrt(tempx**2 + tempy**2)

        data.append(2*math.sqrt((radius**2)-(point**2)))

    q25, q75 = np.percentile(data, [.25, .75])
    bin_width = 2*(q75 - q25)*len(data)**(-1/3)
    bins = round((max(data) - min(data))/bin_width)

    plt.hist(data, weights=np.ones_like(data) / len(data), bins=bins)

    plt.show()

    print("Outer circle points: ", outer, " Inner circle points: ", inner)

    print("Ratio of points: ", round(outer/inner, 2))

########################################################################
# Question 4


radius = int(input("Input Radius: "))

p1()
p2()
p3()
