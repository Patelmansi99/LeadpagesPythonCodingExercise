from dateutil import parser as date_parser
from datetime import timezone

class AnimalTransformer:
    @staticmethod
    def transform(animal):
        # Transform friends: comma-delimited string to array
        friends = animal.get("friends", "")
        animal["friends"] = [f.strip() for f in friends.split(",") if f.strip()] if friends else []
        # Transform born_at: to ISO8601 UTC
        born_at = animal.get("born_at")
        if born_at:
            try:
                dt = date_parser.parse(born_at)
                animal["born_at"] = dt.astimezone(timezone.utc).isoformat()
            except Exception:
                animal["born_at"] = None
        return animal
