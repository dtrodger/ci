import unittest

class Test(unittest.TestCase):

	def test_true(self):
		print "HI"
		self.assertTrue(True)

if __name__ == '__main__':
	unittest.main()
	