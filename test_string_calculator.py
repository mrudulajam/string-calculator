import unittest
from string_calculator import add  # Import the function from your main file

class TestStringCalculator(unittest.TestCase):
	def test_newline_delimiter(self):
		self.assertEqual(add("1\n2,3"), 6)
	
if __name__ == "__main__":
	unittest.main()