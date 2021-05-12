
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np

########################################################################
# 3.1


def p1():

    x1 = [0 for i in range(n)]
    y1 = [0 for i in range(n)]

    radius1 = np.random.uniform(0, radius_limit, n)
    theta1 = np.random.uniform(0, 2*np.pi, n)

    for i in range(n):

        x1[i] = radius1[i] * np.cos(theta1[i])
        y1[i] = radius1[i] * np.sin(theta1[i])

    print("Variation in X coordinates 3.1 -> ", round(np.var(x1), 2))

    plt.scatter(x1, y1, s=1, alpha=1, c=colors, cmap='twilight_shifted')

    circ = plt.Circle((0, 0), radius_limit, color='black', fill=False)
    fig = plt.gcf()
    axes = fig.gca()
    axes.add_patch(circ)

    plt.xlim(-radius_limit*1.2, radius_limit*1.2)
    plt.ylim(-radius_limit*1.2, radius_limit*1.2)

    axes = plt.gca()
    axes.set_aspect('equal')

    plt.show()

########################################################################
# 3.2


def p2():

    x2 = [0 for i in range(n)]
    y2 = [0 for i in range(n)]

    for i in range(n):

        tempx = np.random.uniform(-radius_limit, radius_limit, 1)
        tempy = np.random.uniform(-radius_limit, radius_limit, 1)

        while (np.sqrt(tempx**2 + tempy**2) > radius_limit):

            tempx = np.random.uniform(-radius_limit, radius_limit, 1)
            tempy = np.random.uniform(-radius_limit, radius_limit, 1)

        x2[i] = tempx
        y2[i] = tempy

    print("Variation in X coordinates 3.2-> ", round(np.var(x2), 2))

    plt.scatter(x2, y2, s=1, alpha=1, c=colors, cmap='twilight_shifted')

    circ = plt.Circle((0, 0), radius_limit, color='black', fill=False)
    fig = plt.gcf()
    axes = fig.gca()
    axes.add_patch(circ)

    plt.xlim(-radius_limit*1.2, radius_limit*1.2)
    plt.ylim(-radius_limit*1.2, radius_limit*1.2)

    axes = plt.gca()
    axes.set_aspect('equal')

    plt.show()

########################################################################
# 3.3


def p3():

    x3 = [0 for i in range(n)]
    y3 = [0 for i in range(n)]

    theta3 = np.random.uniform(0, 2*np.pi, n)

    for i in range(n):

        radius3 = np.sqrt(np.random.random()) * radius_limit

        x3[i] = radius3 * np.cos(theta3[i])
        y3[i] = radius3 * np.sin(theta3[i])

    print("Variation in X coordinates 3.3 -> ", round(np.var(x3), 2))

    plt.scatter(x3, y3, s=1, alpha=1, c=colors, cmap='twilight_shifted')

    circ = plt.Circle((0, 0), radius_limit, color='black', fill=False)
    fig = plt.gcf()
    axes = fig.gca()
    axes.add_patch(circ)

    plt.xlim(-radius_limit*1.2, radius_limit*1.2)
    plt.ylim(-radius_limit*1.2, radius_limit*1.2)

    axes = plt.gca()
    axes.set_aspect('equal')

    plt.show()


########################################################################
# Question 3

n = 50000

colors = np.array([i for i in range(n)])

radius_limit = int(input("Input radius limit for all questions: "))

p1()
p2()
p3()
