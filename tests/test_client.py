from unittest import TestCase

from core.client import RestClientV2


class TestRestAdapterV2(TestCase):

    def setUp(self) -> None:
        self.client = RestClientV2()

    def test_get(self):
        self.client.get('devices')

    def test_post(self):
        self.client.post()

    def test_put(self):
        self.client.put()

    def test_delete(self):
        self.client.delete()
