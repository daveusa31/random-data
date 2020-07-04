import os
import sys
import unittest


os.chdir("../")
sys.path[0] = os.getcwd()

import random_data



class RandomTest(unittest.TestCase):
    def test_russian_name_male(self):
        self.assertFalse(str(random_data.russian.names.male()).isdigit())

    def test_russian_name_female(self):
        self.assertFalse(str(random_data.russian.names.female()).isdigit())




if __name__ == "__main__":
    unittest.main()