import unittest
import json2pandases as jps


class MyTestCase(unittest.TestCase):
    def test_json2pandsjs(self):
        self.data = "E:\json2pandas\user.json"
        print (jps.json2pandases(self.data))


if __name__ == '__main__':
    unittest.main()