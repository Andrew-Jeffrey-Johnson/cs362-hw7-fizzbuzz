import unittest
import fizzbuzz

class testCaseFizzBuzz(unittest.TestCase):
	def test_print_1(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[0], 1)

	def test_print_fizz(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[2], "Fizz")

	def test_print_buzz(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[4], "Buzz")

	def test_print_fizzbuzz(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[14], "FizzBuzz")

	def test_print_all_fizz(self):
		for x in range(1,101):
			if (x%3==0 and x%5 != 0):
				self.assertEqual(fizzbuzz.fizzbuzz()[x-1], "Fizz")

	if __name__ == '__main__':
		unittest.main()
