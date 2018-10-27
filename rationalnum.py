class RationalNumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		while True:
			if float(n).is_integer() and float(d).is_integer():
				n = n/2
				d = d/2
			else:
				n = n*2
				d = d*2
				break
		while True:
			if float(n).is_integer() and float(d).is_integer():
				n = n/3
				d = d/3
			else:
				n = n*3
				d = d*3
				break
		return RationalNumber(n, d)

	def __sub__(self, other):
		n = self.n*other.d - self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __mul__(self, other):
		n = self.n*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __truediv__(self, other):
		n = self.n*other.d
		d = self.d*other.n
		return RationalNumber(n, d)

	# complete this first!
	def __str__(self):
		return str(self.n)+"/"+str(self.d)

	__repr__ = __str__ # what does this do?
	"""
	repr is a more "formal" way of representing a string (or at least according to www.pythonforbeginners.com). For example a repr of 'hi' would be "'hi'", while a str would be 'hi'. So I thinking setting these two together ensure that the program would take EXACTLY what is being inputed and making it into a string rather than taking a shortcut and potentially cutting out something important
	"""

def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(2, 6)
	print(a) # 1/2
	print(b) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(a/b) # 3/2

main()