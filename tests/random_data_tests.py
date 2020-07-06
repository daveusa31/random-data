import os
import sys
import unittest


os.chdir("../")
sys.path[0] = os.getcwd()

import random_data



class RandomTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_russian_name_male(self):
        self.assertFalse(str(random_data.russian.names.male()).isdigit())

    def test_russian_name_female(self):
        self.assertFalse(str(random_data.russian.names.female()).isdigit())

    def test_length_password_15(self):
        self.assertEqual(len(random_data.etc.password()), 15)

    def test_length_password_10(self):
        self.assertEqual(len(random_data.etc.password(length=10)), 10)



if __name__ == "__main__":
    unittest.main()