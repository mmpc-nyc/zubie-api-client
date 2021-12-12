from unittest import TestCase
from core.adapter import RestAdapterV2


class TestRestAdapterV2(TestCase):

    def setUp(self) -> None:
        self.adapter = RestAdapterV2

    def test_get(self):
        self.adapter.get()
