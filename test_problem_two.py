import unittest
from problem_two import *



class TestPrintDepth(unittest.TestCase):

    def test_output(self):
        """
        Tests if the value returned from the print_depth function
        matchs the expected value.
        """
        var1 = {
                "key1":1,
                "key2":{
                    "key3":1,
                    "key4":{
                        "key5":4,
                        "user":person_b,
                        }
                    }
                }

        var2 = {"user1": person_a}
        
        self.assertDictEqual(print_depth(var1), {'key1': 1, 'key2': 1, 'key3': 2, 'key4': 2, 'key5': 3, 'user': 3, 'first_name': 5, 'last_name': 5, 'father': 5})
        self.assertDictEqual(print_depth(var2), {'user1':1, 'first_name':2, 'last_name':2, 'father':2})
        self.assertDictEqual(print_depth({}), {})
        


    def test_input_data(self):
        """
        Raises a TypeError if the input data is not a dictionary
        """
        self.assertRaises(TypeError, print_depth, [])
        self.assertRaises(TypeError, print_depth, 1)
        self.assertRaises(TypeError, print_depth, 'test')

