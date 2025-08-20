import unittest
from unittest.mock import patch, MagicMock
from src.animal_api import AnimalAPI

class TestAnimalAPI(unittest.TestCase):
    @patch.object(AnimalAPI, 'robust_request')
    def test_fetch_all_animals(self, mock_robust_request):
        # Simulate two pages
        mock_robust_request.side_effect = [
            MagicMock(json=lambda: {"animals": [{"id": 1}], "next_page": True}),
            MagicMock(json=lambda: {"animals": [{"id": 2}], "next_page": False})
        ]
        api = AnimalAPI(api_base="http://localhost:3123/animals/v1")
        animals = api.fetch_all_animals()
        self.assertEqual(len(animals), 2)
        self.assertEqual(animals[0]["id"], 1)
        self.assertEqual(animals[1]["id"], 2)

    @patch("src.animal_api.requests.request")
    def test_robust_request_retries_on_5xx(self, mock_request):
        # Simulate 2 failures then a success
        resp_fail = MagicMock(status_code=500)
        resp_fail.raise_for_status.side_effect = Exception("fail")
        resp_success = MagicMock(status_code=200)
        resp_success.raise_for_status.return_value = None
        mock_request.side_effect = [resp_fail, resp_fail, resp_success]
        api = AnimalAPI(api_base="http://localhost:3123/animals/v1")
        with patch("time.sleep"):  # skip actual sleep
            resp = api.robust_request("http://test")
        self.assertEqual(resp.status_code, 200)

if __name__ == "__main__":
    unittest.main()
