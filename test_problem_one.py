import unittest
from problem_one import print_depth



class TestPrintDepth(unittest.TestCase):

    def test_output(self):
        var1 = {
                "key1": 1,
                "key2": {
                    "key3": 1,
                    "key4": {
                        "key5": 4
                        }
                    }
                }

        var2 = {
                "tom": 1,
                "angela": 2
                }
        self.assertDictEqual(print_depth(var1),{'key1': 1, 'key2': 1, 'key3': 2, 'key4': 2, 'key5': 3})
        self.assertDictEqual(print_depth(var2),{'tom':1, 'angela':1})
        self.assertDictEqual(print_depth({}), {})


    def test_input_data(self):
        self.assertRaises(TypeError, print_depth, [])
        self.assertRaises(TypeError, print_depth, 1)
        self.assertRaises(TypeError, print_depth, 'test')
