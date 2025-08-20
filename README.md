# Leadpages Python Coding Exercise

## Setup

1. Download and load the Docker image:
   ```sh
   wget https://storage.googleapis.com/lp-dev-hiring/images/lp-programming-challenge-1-1625758668.tar.gz
   docker load -i lp-programming-challenge-1-1625758668.tar.gz
   ```
2. Run the container:
   ```sh
   docker run --rm -p 3123:3123 -ti lp-programming-challenge-1
   ```
3. Ensure the API is running at http://localhost:3123/

## How to Run

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the ETL script:
   ```sh
   python main.py
   ```

## Notes
- The script will fetch, transform, and load all animals as per the challenge instructions.
- Handles server delays and 5xx errors with retries.
