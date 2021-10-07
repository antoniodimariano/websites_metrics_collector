import unittest
from confluent_kafka_producers_wrapper.producer import Producer


class TestKafaProducer(unittest.TestCase):
    """
    This Class tests the produce_message() method of the Product class
    """

    def test_a_produce_message(self):
        message = {
            "url": "http://cloudbased.me",
            "http_status": "200",
            "elapsed_time": "0.2",
            "pattern_verified": "True"
        }

        producer = Producer(topic='websites_metrics')
        ret = producer.produce_message(value=message, key={"service_name": "test"})
        self.assertEqual(ret, {'topic': 'websites_metrics', 'sent': True})
