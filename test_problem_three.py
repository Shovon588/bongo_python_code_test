import unittest
from problem_three import first_node_ancestors, find_lca



class TestFirstNodeAncestors(unittest.TestCase):
    tree = {1:-1, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4}

    def test_output(self):
        self.assertDictEqual(first_node_ancestors(8), {8:True, 4:True, 2:True, 1:True})
        self.assertDictEqual(first_node_ancestors(1), {1:True})


    def test_input_data(self):
        self.assertRaises(KeyError, first_node_ancestors, 50)
        
    

class TestFindLca(unittest.TestCase):
    tree = {1:-1, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4}
    
    def test_output(self):
        self.assertEqual(find_lca(8,9),4)
        self.assertEqual(find_lca(8,7),1)
        self.assertEqual(find_lca(3,7),3)
        

    def test_input_data(self):
        self.assertRaises(KeyError)
