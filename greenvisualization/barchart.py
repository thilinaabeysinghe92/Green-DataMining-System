import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class barchart():
    """docstring fo Barchart."""
    def __init__(self):
        print "Hello"

    def setFile(self, filepath):
        self.filepath = filepath

    def setName(self, name):
        self.name = name

    def setX(self, x):
        self.X = x



    def setY(self, y):
        self.Y = y

    def greenCSVRead(self):
        df = pd.read_csv(self.filepath, index_col=False, header=0)
        df1 = df[self.X]
        self.Y = df1
        print df1


    def plotGraph(self):
        self.greenCSVRead()

        plt.rcdefaults()
        fig, ax = plt.subplots()

        # Example data
        people = range(0, 13)
        y_pos = np.arange(len(people))
        #performance = 3 + 10 * np.random.rand(len(people))
        performance = np.array(self.Y[:13])
        print performance
        error = np.random.rand(len(people))

        ax.barh(y_pos, performance, xerr=error, align='center',
                color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Performance')
        ax.set_title('How fast do you want to go today?')

        plt.show()
