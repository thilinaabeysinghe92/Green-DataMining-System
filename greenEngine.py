import sys
sys.path.insert(0, './greenvisualization')
sys.path.insert(1, './greenLanguage')
from barchart import barchart

test = barchart()
test.setFile("data/sample2.csv")
xheadrs = ['score']
test.setX(xheadrs)
test.plotGraph()
