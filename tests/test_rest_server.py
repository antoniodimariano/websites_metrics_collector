import unittest
import requests


class TestRestServer(unittest.TestCase):
    """
    This Class tests the REST Server and the POST method
    """

    def test_a_send_valid_post_request(self):
        payload = [
            [
                "http://cloudbased.me",
                [
                    "Microservices",
                    "Antonio"
                ]
            ],
            [
                "http://ferrari.com",
                [
                    "ferrari"
                ]
            ],
            [
                "http://motoguzzi.com",
                [
                    "aquila"
                ]
            ]
        ]
        response = requests.post("http://127.0.0.1:8080/api/v1/websites_metrics", json=payload)
        self.assertEqual(response.status_code, 201)
        to_match = {'submitted': True,
                    'urls': [['http://cloudbased.me', ['Microservices', 'Antonio']],
                             ['http://ferrari.com', ['ferrari']],
                             ['http://motoguzzi.com', ['aquila']]]}
        self.assertEqual(response.json(), to_match)

    def test_b_send_no_payload(self):
        response = requests.post("http://127.0.0.1:8080/api/v1/websites_metrics")
        self.assertEqual(response.status_code, 403)
        self.assertIsInstance(response.json(),dict)

    def test_c_send_empty_list(self):
        response = requests.post("http://127.0.0.1:8080/api/v1/websites_metrics",json=[])
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json(),dict)

    def test_c_send_empty_dict(self):
        response = requests.post("http://127.0.0.1:8080/api/v1/websites_metrics",json={})
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json(),dict)



