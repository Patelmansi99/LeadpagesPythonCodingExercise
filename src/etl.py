from src.animal_api import AnimalAPI
from src.animal_transformer import AnimalTransformer

class AnimalETL:
    def __init__(self, api, transformer, batch_size=100):
        self.api = api
        self.transformer = transformer
        self.batch_size = batch_size

    def run(self):
        print("Fetching animal list...")
        animal_refs = self.api.fetch_all_animals()
        print(f"Found {len(animal_refs)} animals.")
        details = []
        for ref in animal_refs:
            details.append(self.transformer.transform(self.api.fetch_animal_detail(ref["id"])))
            if len(details) % 25 == 0:
                print(f"Fetched {len(details)} details...")
        print("Posting batches...")
        for i in range(0, len(details), self.batch_size):
            batch = details[i:i+self.batch_size]
            self.api.post_animals_batch(batch)
        print("Done!")
