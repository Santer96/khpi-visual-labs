import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def task1_1():
    X = np.linspace(0, math.pi, 200)
    Y = [(math.cos(5 * math.pi * x) * (math.sin(3 * math.pi * x)) ** 2)
         + (3 * math.sin(math.pi * x) * math.cos(3 * math.pi * x) ** 3) for x in X]
    plt.plot(X, Y)
    plt.show()


def task1_2():
    X = np.linspace(-10, 2.5, 300)
    X1 = X[X <= 0]
    X2 = X[X > 0]
    Y1 = [math.sqrt(1 + x ** 2) for x in X1]
    Y2 = [(1 + x ** 3) / ((1 + (1 + (math.e ** (-0.5 * x)))) ** (1/5)) for x in X2]
    Y = Y1 + Y2
    plt.plot(X, Y)
    plt.show()


def task2():
    x = np.outer(np.linspace(-20, 20, 64), np.ones(64))
    y = x.copy().T  # transpose
    z = ((10 * (x ** 2) * (np.cos(x) ** 5)) - (2 * (y ** 3)))
    plt.figure(figsize=(14, 9))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z)
    plt.show()


def task3():
    fi = np.arange(-1.5, 1.5, 0.01)
    r = np.sqrt(np.cos(2 * fi) + np.sqrt((np.cos(2 * fi) ** 2)))
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(r, fi)
    ax.set_rmax(1.5)
    plt.show()


def task4():
    x = np.outer(np.linspace(-10, 10, 32), np.ones(32))
    y = x.copy().T  # transpose
    z = ((x ** 2) - (y ** 2) / 2)
    plt.figure(figsize=(14, 9))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z)
    plt.show()


index = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
data = [[76.4, 45.7, 40.8, 44, 123], [97.6, 54.7, 41.8, 51.6, 158], [122.2, 58.7, 42, 63.2, 171.5],
        [130.5, 62.3, 42, 71.8, 186.5], [153, 67, 42, 83, 205.5], [176, 72, 46, 93, 226.5],
        [200.5, 77, 50.5, 104, 247], [227, 75.5, 54, 116.8, 258.5], [247, 79, 56.5, 123.5, 290], [277, 82, 59, 127, 290]]
df = pd.DataFrame(data, columns=['USA', 'Germany', 'France', 'Japan', "ussr"], index=index)


def task5_1():
    df.plot.bar(rot=0)
    plt.show()


def task5_2():
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    # position
    x1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
          3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
          4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
          5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    z1 = np.zeros(50)

    # length and width
    dx1 = np.ones(50)
    dy1 = np.ones(50)

    # value
    dz1 = [76.4, 97.6, 122.2, 130.5, 153, 176, 200.5, 227, 247, 277,
           45.7, 54.7, 58.7, 62.3, 67, 72, 77, 75.5, 79, 82,
           40.8, 41.8, 42, 42, 42, 46, 50.5, 54, 56.5, 59,
           44, 51.6, 63.2, 71.8, 83, 93, 104, 116.8, 123.5, 127,
           123, 158, 171.5, 186.5, 205.5, 226.5, 247, 258.5, 290, 290]

    # labels
    ax1.set_yticks([1.5, 2.5, 3.5, 4.5, 5.5])
    ax1.set_yticklabels(['USA', 'Germany', 'France', 'Japan', "ussr"])

    ax1.bar3d(y1, x1, z1, dx1, dy1, dz1)
    plt.show()

#
# task1_1()
# task1_2()
# task2()
task3()
# task4()
# task5_1()
# task5_2()
