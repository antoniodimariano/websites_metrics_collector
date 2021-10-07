import unittest
from unittest import IsolatedAsyncioTestCase
from websites_metrics_collector.communication import webpages_fetcher
class Test(IsolatedAsyncioTestCase):
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
    async def test_c_fetch_with_valid_list_of_url(self):
        urls_to_fetch = [('http://sjsjsjjsjsjsjsj.com', ['twitter', 'Antonio'])]

        ret = await webpages_fetcher.fetch_list_of_urls(list_of_urls=urls_to_fetch)
        self.assertIsInstance(ret,list)
        self.assertEqual(len(ret),1)
        self.assertEqual(ret[0].url,'http://sjsjsjjsjsjsjsj.com')
        self.assertEqual(ret[0].http_status,403)
        self.assertIsInstance(ret[0].elapsed_time,float)
        self.assertIsInstance(ret[0].pattern_verified,bool)
        self.assertEqual(ret[0].pattern_verified,False)


