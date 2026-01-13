import unittest
from playwright.sync_api import sync_playwright
from tests.test_data import POSITIVE_TEST_DATA, NEGATIVE_TEST_DATA


class TestMunicipalitiesByName(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = "https://local-gov-units.polandapi.com"
        cls.playwright = sync_playwright().start()
        cls.request = cls.playwright.request.new_context(
            base_url=cls.base_url,
            ignore_https_errors=True
        )

    @classmethod
    def tearDownClass(cls):
        cls.request.dispose()
        cls.playwright.stop()

    # -------- POSITIVE TESTS --------

    def test_positive_municipality_name(self):
        for data in POSITIVE_TEST_DATA:
            with self.subTest(city=data["city"]):
                response = self.request.get(
                    f"/api/v1/municipalities/name/{data['city']}"
                )

                self.assertEqual(response.status, 200)

                body = response.json()

                self.assertTrue(body["success"])
                self.assertTrue(len(body["data"]) > 0)

    # -------- NEGATIVE TESTS --------

    def test_negative_municipality_name(self):
        for data in NEGATIVE_TEST_DATA:
            with self.subTest(city=data["city"]):
                response = self.request.get(
                    f"/api/v1/municipalities/name/{data['city']}"
                )

                self.assertEqual(response.status, 200)

                body = response.json()

                self.assertFalse(body["success"])
                self.assertEqual(len(body["data"]), 0)