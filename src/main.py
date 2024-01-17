from scripts.scraper import scrape_job_listings
from scripts.data_processor import save_data
from scripts.data_analyzer import analyze_data


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

    all_data = []

    for lang in languages:
        url = f"https://www.saramin.co.kr/zf_user/search?searchword={lang}"
        job_count = scrape_job_listings(url)
        print(f"{lang}: {job_count}")
        all_data.append({"language": lang, "job_count": job_count})

    # 모든 데이터를 하나의 파일에 저장
    save_data(all_data, "all_languages")

    # 데이터 분석 및 시각화 호출
    analyze_data("C:\\Users\\csb12\\CodeTrend\\data\\all_languages.json")


if __name__ == "__main__":
    main()
