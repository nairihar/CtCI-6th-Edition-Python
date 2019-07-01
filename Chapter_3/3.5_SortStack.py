import unittest
from utils.stack import Stack


def sortStack(s1, s2):
	if s2.isEmpty():
		s2.push(s1.pop())

	last_n = s2.getLast()

	while not s1.isEmpty():
		poped_n = s1.pop()
		if poped_n > last_n:
			last_n = poped_n
			s2.push(poped_n)
		else:
			c = 0
			while not s2.isEmpty() and poped_n < s2.getLast():
				s1.push(s2.pop())
				c += 1
			s2.push(poped_n)
			while c > 0:
				c -= 1
				s2.push(s1.pop())
			last_n = s2.getLast()
	return s2


class Test(unittest.TestCase):
	'''Test Cases'''

	def test(self):
		s1 = Stack()

		s1.push(7)
		s1.push(10)
		s1.push(5)

		s2 = Stack()

		s2.push(1)
		s2.push(3)
		s2.push(8)
		s2.push(12)

		s = sortStack(s1, s2)
		self.assertListEqual(s.getFullArray(), [1, 3, 5, 7, 8, 10, 12])

		s3 = Stack()

		s3.push(7)
		s3.push(10)
		s3.push(5)

		s4 = Stack()

		ss = sortStack(s3, s4)

		self.assertListEqual(ss.getFullArray(), [5, 7, 10])


if __name__ == "__main__":
	unittest.main()
