import unittest
import json2pandas as jp


class MyTestCase(unittest.TestCase):
    def test_json2pandas(self):
        self.data = "E:\json2pandas\user.json"
        print (jp.json2pandas(self.data))


if __name__ == '__main__':
    unittest.main()