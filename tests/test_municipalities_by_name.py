import unittest
from playwright.sync_api import sync_playwright


class TestMunicipalitiesByName(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = "https://local-gov-units.polandapi.com"
        cls.playwright = sync_playwright().start()
        cls.request = cls.playwright.request.new_context(
            base_url=cls.base_url,
            ignore_https_errors=True  # API uses expired SSL certificate
        )

    @classmethod
    def tearDownClass(cls):
        cls.request.dispose()
        cls.playwright.stop()

    # ---------- POSITIVE TESTS ----------

    def test_get_municipality_by_name_lodz_should_return_data(self):
        response = self.request.get(
            "/api/v1/municipalities/name/Lodz"
        )

        self.assertEqual(response.status, 200)

        body = response.json()
        self.assertTrue(body["success"])
        self.assertGreater(len(body["data"]), 0)

    def test_get_municipality_by_name_warszawa_should_return_data(self):
        response = self.request.get(
            "/api/v1/municipalities/name/Warszawa"
        )

        self.assertEqual(response.status, 200)

        body = response.json()
        self.assertTrue(body["success"])
        self.assertGreater(len(body["data"]), 0)

    # ---------- NEGATIVE TESTS ----------

    def test_get_municipality_by_non_existing_name_should_return_404(self):
        response = self.request.get(
            "/api/v1/municipalities/name/ytrytr"
        )

        self.assertEqual(response.status, 404)

        body = response.json()
        self.assertFalse(body["success"])
        self.assertEqual(len(body["data"]), 0)

    def test_get_municipality_by_invalid_name_should_return_404(self):
        response = self.request.get(
            "/api/v1/municipalities/name/zzzzzz"
        )

        self.assertEqual(response.status, 404)

        body = response.json()
        self.assertFalse(body["success"])
        self.assertEqual(len(body["data"]), 0)