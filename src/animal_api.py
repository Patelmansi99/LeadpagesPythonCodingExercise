import requests
import time

class AnimalAPI:
    def __init__(self, api_base, max_retries=5, retry_backoff=2):
        self.api_base = api_base
        self.max_retries = max_retries
        self.retry_backoff = retry_backoff

    def robust_request(self, url, method="get", **kwargs):
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = requests.request(method, url, timeout=30, **kwargs)
                if resp.status_code in {500, 502, 503, 504}:
                    raise requests.HTTPError(f"Server error: {resp.status_code}")
                resp.raise_for_status()
                return resp
            except (requests.RequestException, requests.HTTPError) as e:
                print(f"Request failed ({e}), attempt {attempt}/{self.max_retries}. Retrying...")
                time.sleep(self.retry_backoff * attempt)
        raise Exception(f"Failed to fetch {url} after {self.max_retries} attempts.")

    def fetch_all_animals(self):
        animals = []
        page = 1
        while True:
            resp = self.robust_request(f"{self.api_base}/animals", params={"page": page})
            data = resp.json()
            animals.extend(data["animals"])
            if not data.get("next_page"):
                break
            page += 1
        return animals

    def fetch_animal_detail(self, animal_id):
        resp = self.robust_request(f"{self.api_base}/animals/{animal_id}")
        return resp.json()

    def post_animals_batch(self, batch):
        url = f"{self.api_base}/home"
        resp = self.robust_request(url, method="post", json=batch)
        print(f"Posted batch of {len(batch)} animals. Status: {resp.status_code}")
