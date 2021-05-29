import unittest
import fizzbuzz

class testCaseFizzBuzz(unittest.TestCase):
	def test_print_1(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[0], 1)

	def test_print_fizz(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[2], "Fizz")

	def test_print_buzz(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[4], "Buzz")

	def test_print_buzz(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[14], "FizzBuzz")

	if __name__ == '__main__':
		unittest.main()
