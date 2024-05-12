import requests
import threading
import random
from time import sleep

BASE_URL = "http://localhost:8000"

def book_event(event_id, user_id):
    url = f"{BASE_URL}/{event_id}/{user_id}"
    response = requests.get(url)
    print(f"Request for event {event_id} and user {user_id}: {response.json()}")

def simulate_double_booking(event_id, num_requests):
    threads = []
    for _ in range(num_requests):
        user_id = random.randint(1, 5)  # Generate a random user_id between 1 and 5
        thread = threading.Thread(target=book_event, args=(event_id, user_id))
        threads.append(thread)
        thread.start()
        sleep(0.01)  # Delay to ensure all threads start around the same time

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    event_id = 1
    num_requests = 500

    simulate_double_booking(event_id, num_requests)