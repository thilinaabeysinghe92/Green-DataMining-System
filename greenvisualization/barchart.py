import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Barchart(object):
    """docstring fo Barchart."""
    def __init__(self):
        print "Hello"

    def setFile(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath

    def setName(self, name):
        self.name = name

    def setX(self, x):
        self.X = x


    def setY(self, y):
        self.Y = y

    def greenCSVRead(self):
        df = pd.read_csv(self.path, index_col=False, header=0)
        df1 = df[[self.X]]
        self.Y = df1

    def plotGraph(self):
        greenCSVRead()

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        xAxis = self.X
        y_pos = np.arange(len(xAxis))
        performance = self.Y
        error = np.random.rand(len(xAxis))

        ax.barh(y_pos, performance, xerr=error, align='center',
                color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(xAxis)
        ax.invert_yaxis()  # labels read top-to-bottom


        plt.show()
