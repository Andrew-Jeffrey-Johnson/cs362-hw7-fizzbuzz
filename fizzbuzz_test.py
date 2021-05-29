import unittest
import fizzbuzz

class testCaseFizzBuzz(unittest.TestCase):
	def test_print_100(self):
		self.assertEqual(fizzbuzz.fizzbuzz()[1], 1)

	if __name__ == '__main__':
		unittest.main()