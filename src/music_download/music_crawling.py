from selenium import webdriver
import numpy as np
import pandas as pd
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

music_df = pd.read_csv('././data/processed_data/daily_charts_track_list.csv')

j=0
for i in range(1002,1130):
    j+=1
    if j==5:
        music_df.to_csv('././data/processed_data/daily_charts_track_list.csv', index=False)
        j=0
    driver = webdriver.Chrome()
    artist = music_df['artist_names'].iloc[i]
    track = music_df['track_name'].iloc[i]
    # 뮤직비디오 검색
    driver.get(f'https://www.youtube.com/results?search_query={artist}+{track}')

    # 뮤직비디오 클릭한 다음 url 가져오기
    element = driver.find_element(By.CSS_SELECTOR, "a#thumbnail")
    element.click()
    url = driver.current_url
    music_df.at[i, 'url'] = url
    print(url)
    driver.quit()
music_df.to_csv('././data/processed_data/daily_charts_track_list.csv', index=False)
