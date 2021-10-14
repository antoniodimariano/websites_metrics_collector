import unittest
import requests
from unittest import IsolatedAsyncioTestCase
from websites_metrics_collector.communication import webpages_fetcher
from websites_metrics_collector.helpers.regex_functions import check_patterns_in_webpage
from websites_metrics_collector.classes.Driver import Driver

class Test(IsolatedAsyncioTestCase):
    """
    This Class tests the Driver() method produce_metrics_for_websites()
    that is the high-level method called to collect and produce metrics.
    """

    async def test_a_fetch_with_valid_list_of_url(self):
        urls_to_fetch = [('http://motoguzzi.com', ['twitter', 'Antonio']), ('http://ducati.com', ['twitter', 'url']),
                         ('http://ferrari.com', ['twitter', 'url'])]

        driver = Driver('websites_metrics')
        ret = await driver.produce_metrics_for_websites(list_of_urls_to_check=urls_to_fetch,produce_message=0)
        self.assertIsInstance(ret, list)
        self.assertEqual(len(ret), 3)
        self.assertEqual(ret[0].url, 'http://motoguzzi.com')
        self.assertEqual(ret[0].http_status, 200)
        self.assertIsInstance(ret[0].elapsed_time, float)
        self.assertIsInstance(ret[0].pattern_verified, bool)

class TestFetching_From_Websites(IsolatedAsyncioTestCase):
    """
    This Class tests the fetch_list_of_urls() async method used to fetch URLs
    """

    async def test_a_fetch_with_valid_list_of_url(self):
        urls_to_fetch = [('http://motoguzzi.com', ['twitter', 'Antonio']), ('http://ducati.com', ['twitter', 'url']),
                         ('http://ferrari.com', ['twitter', 'url'])]

        ret = await webpages_fetcher.fetch_list_of_urls(list_of_urls=urls_to_fetch)
        self.assertIsInstance(ret,list)
        self.assertEqual(len(ret),3)
        self.assertEqual(ret[0].url,'http://motoguzzi.com')
        self.assertEqual(ret[0].http_status,200)
        self.assertIsInstance(ret[0].elapsed_time,float)
        self.assertIsInstance(ret[0].pattern_verified,bool)


    async def test_b_fetch_with_valid_list_of_url(self):
        urls_to_fetch = [('http://motoguzzi.com', ['twitter', 'Antonio'])]

        ret = await webpages_fetcher.fetch_list_of_urls(list_of_urls=urls_to_fetch)
        self.assertIsInstance(ret,list)
        self.assertEqual(len(ret),1)
        self.assertEqual(ret[0].url,'http://motoguzzi.com')
        self.assertEqual(ret[0].http_status,200)
        self.assertIsInstance(ret[0].elapsed_time,float)
        self.assertIsInstance(ret[0].pattern_verified,bool)
    @unittest.skip
    async def test_c_fetch_with_valid_list_of_url(self): #pragma no cover
        urls_to_fetch = [('http://sjsjsjjsjsjsjsj.com', ['twitter', 'Antonio'])]

        ret = await webpages_fetcher.fetch_list_of_urls(list_of_urls=urls_to_fetch)
        self.assertIsInstance(ret,list)
        self.assertEqual(len(ret),1)
        self.assertEqual(ret[0].url,'http://sjsjsjjsjsjsjsj.com')
        self.assertEqual(ret[0].http_status,403)
        self.assertIsInstance(ret[0].elapsed_time,float)
        self.assertIsInstance(ret[0].pattern_verified,bool)
        self.assertEqual(ret[0].pattern_verified,False)

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


if __name__ == "__main__": #pragma no cover
    unittest.main()