import json


def save_data(data, filename):
    with open(f"data/{filename}.json", "w") as file:
        json.dump(data, file)
