import unittest
from unittest.mock import MagicMock
from src.etl import AnimalETL

class DummyAPI:
    def __init__(self):
        self.fetch_all_animals_called = False
        self.fetch_animal_detail_called = 0
        self.posted_batches = []
    def fetch_all_animals(self):
        self.fetch_all_animals_called = True
        return [{"id": 1}, {"id": 2}]
    def fetch_animal_detail(self, animal_id):
        self.fetch_animal_detail_called += 1
        return {"id": animal_id, "friends": "a, b", "born_at": "2020-01-01T00:00:00Z"}
    def post_animals_batch(self, batch):
        self.posted_batches.append(batch)

class DummyTransformer:
    def transform(self, animal):
        animal["transformed"] = True
        return animal

class TestAnimalETL(unittest.TestCase):
    def test_etl_run(self):
        api = DummyAPI()
        transformer = DummyTransformer()
        etl = AnimalETL(api, transformer, batch_size=1)
        etl.run()
        self.assertTrue(api.fetch_all_animals_called)
        self.assertEqual(api.fetch_animal_detail_called, 2)
        self.assertEqual(len(api.posted_batches), 2)
        for batch in api.posted_batches:
            self.assertTrue(batch[0]["transformed"])

if __name__ == "__main__":
    unittest.main()
