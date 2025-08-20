import unittest
from src.animal_transformer import AnimalTransformer

class TestAnimalTransformer(unittest.TestCase):
    def test_transform_friends_and_born_at(self):
        animal = {
            "friends": "cat, dog, fish ",
            "born_at": "2020-01-01T12:00:00-05:00"
        }
        result = AnimalTransformer.transform(animal.copy())
        self.assertEqual(result["friends"], ["cat", "dog", "fish"])
        self.assertTrue(result["born_at"].endswith("Z") or "+00:00" in result["born_at"])  # UTC

    def test_transform_empty_friends(self):
        animal = {"friends": "", "born_at": None}
        result = AnimalTransformer.transform(animal.copy())
        self.assertEqual(result["friends"], [])
        self.assertIsNone(result["born_at"])

if __name__ == "__main__":
    unittest.main()
