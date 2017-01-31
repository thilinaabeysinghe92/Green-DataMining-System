from barchart import barchart

test = barchart()
test.setFile("data/sample2.csv")
xheadrs = ['score']
test.setX(xheadrs)
test.plotGraph()
