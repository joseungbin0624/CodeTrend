import json


def save_data(data, filename):
    # 모든 데이터를 하나의 JSON 파일로 저장
    with open(f"data/{filename}.json", "w") as file:
        json.dump(data, file)
