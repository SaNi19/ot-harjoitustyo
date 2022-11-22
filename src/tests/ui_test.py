import unittest
from ui import UI

class TestUi(unittest.TestCase):
    def setUp(self):
	print("Test")

    def test_ui(self):
	answer = str(self._root)
	self.assertEqual(answer, "None")
