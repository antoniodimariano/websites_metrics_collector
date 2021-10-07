import unittest
import requests
from helpers.regex_functions import check_patterns_in_webpage


class TestPattern(unittest.TestCase):
    """
    This Class tests the validation of a regexp in a HTML page
    """
    def test_a_valid_pattern_in_text(self):
        response = requests.get('http://cloudbased.me')
        ret = check_patterns_in_webpage(response.text, patterns=['Antonio Di Mariano', 'Ghost'])
        self.assertIs(ret, True)

    def test_b_not_valid_pattern_in_text(self):
        response = requests.get('http://cloudbased.me')
        ret = check_patterns_in_webpage(response.text, patterns=['Dragon', 'Homer Simpson'])
        self.assertIs(ret, False)

    def test_c_valid_pattern_in_text(self):
        response = requests.get('http://cloudbased.me')
        ret = check_patterns_in_webpage(response.text, patterns=['Antonio Di Mariano'])
        self.assertIs(ret, True)

    def test_d_valid_empty_list_pattern_in_text(self):
        response = requests.get('http://cloudbased.me')
        ret = check_patterns_in_webpage(response.text, patterns=[])
        self.assertIs(ret, True)

    def test_e_not_valid_string_pattern_in_text(self):
        response = requests.get('http://cloudbased.me')
        ret = check_patterns_in_webpage(response.text, patterns='ciao')
        self.assertIs(ret, False)
if __name__ == "__main__":
    unittest.main()