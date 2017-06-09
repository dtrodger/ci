import unittest

class Test(unittest.TestCase):

	def test_true(self):
		print "HELLO"
		self.assertTrue(True)

if __name__ == '__main__':
	unittest.main()

# Docker w/ nginx
# output status of test to web app
# deploy rails app to server
# tool that mocks interface of sqs so in unittest we are not sending request to amazon, but send reuqest to app or service thats running locally to imitate sqs
	