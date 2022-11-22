import unittest
from ui import UI

class TestUi(unittest.TestCase):
    def setUp(self):
	print("Test")

    def test_ui(self):
	vastaus = str(self._root)
	self.assertEqual(vastaus, "None")
