from unittest import IsolatedAsyncioTestCase
from classes.Driver import Driver


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
