import unittest
import fizzbuzz

class testCaseFizzBuzz(unittest.TestCase):
	def test_print_1(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[0], 1)

	def test_print_100(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[2], "Fizz")

	if __name__ == '__main__':
		unittest.main()
