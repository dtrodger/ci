import unittest

class Test(unittest.TestCase):

	def test_true(self):
		self.assertTrue(True)

	def test_false(self):
		self.assertFalse(False)

if __name__ == '__main__':
	unittest.main()

# Docker w/ nginx
# output status of test to web app
# deploy rails app to server
# tool that mocks interface of sqs so in unittest we are not sending request to amazon, but send reuqest to app or service thats running locally to imitate sqs
	