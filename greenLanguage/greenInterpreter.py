import sys
sys.path.insert(0, '../greenvisualization')
from barchart import barchart

class Token(object):
	def __init__(self ,type ,name ,value):
		self.type = type
		self.name = name
		self.value = value

class Interpreter(object):
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.current_token = None

	def token_line(self):
		lines = self.text.split(';')
		return lines

	def token_in_line(self, lines):
		for i in range(0,len(lines)):
			self.current_line = lines[i]
			keywords = self.current_line.split(' ')


			if keywords[0] == 'file':
				filename = keywords[1]
				columnname = keywords[2]
				print("I got file %s " % filename)
				bar_chart = barchart()
				bar_chart.setFile(filename)
				xheadrs = [columnname]
				bar_chart.setX(xheadrs)
				bar_chart.plotGraph()

			

def main():
	while True:
		text = raw_input('Green> ')
		interpreter = Interpreter(text)
		lines = interpreter.token_line()
		interpreter.token_in_line(lines)



if __name__ == '__main__':
	main()
