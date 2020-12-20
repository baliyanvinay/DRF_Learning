from django.test import TestCase
from rest_framework.test import RequestsClient
import json
import requests


class RestTestCase(TestCase):

    def setUp(self):
        self.test_1 = []
        with open('TestData/http001.json') as f:
            for line in f:
                self.test_1.append(line)

    def test_get_all_wishes(self):
        client = RequestsClient()
        for ro in self.test_1:
            row = json.loads(ro)
            print(row)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['response']['body'] != {}:
                response = json.loads(res.text)
                self.assertEqual(response, row['response']['body'])
