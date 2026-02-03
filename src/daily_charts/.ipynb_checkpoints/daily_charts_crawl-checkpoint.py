from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pandas import date_range
import os, time

def get_daily_charts_csv():
    service = Service()
    options = Options()

    # 다운로드 경로 설정
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    download_path = os.path.abspath(os.path.join(cur_dir, '../../data/raw_data'))
    prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://charts.spotify.com/login?flow_ctx=fe0da8d1-7466-4ee4-8c2e-fb86e5e27f5c%3A1769857143")
        input("로그인을 완료하고 차트 페이지가 보이면 엔터를 눌러주세요.")

        dates = date_range(start='2025-01-01', end='2025-12-31').strftime('%Y-%m-%d')
        for date in dates:
            # 중복 파일이 있으면 건너뛰기
            file_name = f'regional-kr-daily-{date}.csv'
            if os.path.exists(os.path.join(download_path, file_name)):
                continue

            url = f'https://charts.spotify.com/charts/view/regional-kr-daily/{date}'
            try:
                driver.get(url)
                time.sleep(2)

                # csv 다운로드 버튼 선택 및 클릭
                download_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-labelledby="csv_download"]')
                download_btn.click()

                print(f'{date} 데이터 다운로드 성공')
                time.sleep(10)  # 해당 시간이 너무 짧으면 드라이버 과부화로 오류 발생

            except Exception as e:
                print(f'{date} 데이터 다운로드 실패: {e}')
                continue
    
    except Exception as e:
        print(f'크롤링 프로세스 시작 실패: {e}')

    finally:
        driver.quit()
        print('크롤링 프로세스 종료')

if __name__ == '__main__':
    get_daily_charts_csv()