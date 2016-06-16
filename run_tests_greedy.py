import unittest
import tests_greedy as tests

class TestGreedyNavigator(unittest.TestCase):

	def test_graph1(self):
		self.assertEqual(tests.test1('greedy', 1, 5), [1,3,4,5]);

	def test_graph2(self):
		self.assertEqual(tests.test2('greedy', 1, 5), [1,3,4,5]);

	def test_graph3(self):
		self.assertEqual(tests.test3('greedy', 7, 5), [7,3,0,1,5])

	def test_graph4(self):
		self.assertEqual(tests.test3('greedy', 7, 8), [7,3,4,8])

if __name__ == "__main__":
	unittest.main()
	
	
