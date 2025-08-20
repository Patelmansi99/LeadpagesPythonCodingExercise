def fetch_all_animals():
def fetch_animal_detail(animal_id):
def robust_request(url, method="get", **kwargs):
def transform_animal(animal):
def post_animals_batch(batch):
def main():

from src.animal_api import AnimalAPI
from src.animal_transformer import AnimalTransformer
from src.etl import AnimalETL

API_BASE = "http://localhost:3123/animals/v1"
BATCH_SIZE = 100

def main():
    api = AnimalAPI(api_base=API_BASE)
    transformer = AnimalTransformer()
    etl = AnimalETL(api, transformer, batch_size=BATCH_SIZE)
    etl.run()

if __name__ == "__main__":
    main()
