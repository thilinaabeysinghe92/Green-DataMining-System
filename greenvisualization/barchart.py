import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class Barchart(object):
    """docstring fo Barchart."""
    def __init__(self):

    def setFile(self, filename, filepath):
        self.filename = filename
        self.filepath = filepath

    def setName(self, name):
        self.name = name

    def setX(self, x, label):
        self.X = x
        self.xLabel = label

    def setY(self, y):
        self.Y = y

    def plotGraph(self):
        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        xAxis = self.X
        y_pos = np.arange(len(xAxis))
        performance = 3 + 10 * np.random.rand(len(xAxis))
        error = np.random.rand(len(xAxis))

        ax.barh(y_pos, performance, xerr=error, align='center',
                color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(xAxis)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel(self.xLabel)
        ax.set_title(self.name)

        plt.show()
