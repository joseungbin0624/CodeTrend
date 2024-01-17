from scripts.scraper import scrape_job_listings
from scripts.data_processor import save_data


def main():
    languages = [
        "Java",
        "Python",
        "C++",
        "C#",
        "JavaScript",
        "PHP",
        "Swift",
        "Ruby",
        "Go",
        "Kotlin",
        "TypeScript",
    ]
    for lang in languages:
        url = f"https://www.saramin.co.kr/zf_user/search?searchword={lang}"
        job_count = scrape_job_listings(url)
        print(f"{lang}: {job_count}개의 채용 공고")
        save_data({lang: job_count}, lang.lower())


if __name__ == "__main__":
    main()
