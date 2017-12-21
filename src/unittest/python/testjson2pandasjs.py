import unittest
import json2pandasjs as jp


class MyTestCase(unittest.TestCase):
    def test_json2pandsjs(self):
        self.data = "E:\json2pandas\BaseIos2.json"
        print (jp.json2pandasjs(self.data))


if __name__ == '__main__':
    unittest.main()