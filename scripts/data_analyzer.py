import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def analyze_data(file_path):
    # 한글 폰트 설정
    plt.rcParams["font.family"] = "NanumGothic"
    # 또는 다른 한글 지원 폰트를 사용할 수 있습니다.

    # JSON 파일을 Pandas DataFrame으로 로드
    df = pd.read_json(file_path)

    # 프로그래밍 언어별 채용 공고 수 계산
    job_counts = df.groupby("language")["job_count"].sum()

    # 데이터 시각화
    plt.figure(figsize=(10, 6))
    job_counts.plot(kind="bar")
    plt.title("프로그래밍 언어별 채용 공고 수")
    plt.xlabel("프로그래밍 언어")
    plt.ylabel("공고 수")
    plt.show()


# 예시 사용 방법
# analyze_data('path_to_your_data_file.json')
