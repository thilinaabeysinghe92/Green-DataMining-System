INTEGER, PLUS, EOF, FILE = 'INTERGER', 'PLUS', 'EOF','FILE'

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
				self.name = keywords[1]
				self.operation = keywords[2]
				self.value = keywords[3]
				self.execute(keywords)

	def execute(self, line):
		if line[0] == 'file':
			print("I got file %s " % line[1])

def main():
	while True:
		text = raw_input('Green> ')
		interpreter = Interpreter(text)
		lines = interpreter.token_line()
		interpreter.token_in_line(lines)



if __name__ == '__main__':
	main()
