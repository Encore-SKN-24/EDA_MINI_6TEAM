# import numpy as np
import pandas as pd

music_detail = pd.read_csv('../../data/processed_data/music_detail_data.csv')
daily_charts= pd.read_csv('../../data/processed_data/daily_charts_analyze.csv')

# music_detail 기준으로 csv 병합
merged_csv = music_detail.merge(daily_charts, on=['artist_names', 'track_name'], how='left')

# 컬럼 'music_id'를 첫 번째 컬럼으로 수정
other_columns = []
for col in merged_csv.columns:
    if col != 'music_id':
        other_columns.append(col)

new_column_order = ['music_id'] + other_columns
merged_csv = merged_csv[new_column_order]

# 병합한 파일을 csv로 변환
merged_csv.to_csv('../../data/processed_data/merged_music.csv', index=False, encoding='utf-8')

print("병합 완료")