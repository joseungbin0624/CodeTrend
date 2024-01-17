import requests
from bs4 import BeautifulSoup
import re


def scrape_job_listings(url):
    # 주어진 URL에서 채용 정보를 스크래핑
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    cnt_result_tag = soup.find("span", class_="cnt_result")
    if cnt_result_tag:
        job_count = re.search(r"\d[\d,]*", cnt_result_tag.text).group().replace(",", "")
        return int(job_count)
    return 0
