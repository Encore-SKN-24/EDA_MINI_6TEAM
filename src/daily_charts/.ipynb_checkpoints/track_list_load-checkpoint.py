import pandas as pd
import os

def load_track_list():
    try:
        # 데이터 로드
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(cur_dir, f'../../data/processed_data/spotify_2025_daily_charts.csv')

        df = pd.read_csv(data_path)

        # 트랙 리스트 생성
        track_list = df[['artist_names', 'track_name']].drop_duplicates(subset=['artist_names', 'track_name'], ignore_index=True)

        # 트랙 리스트 저장
        output_folder = './data/processed_data'
        path = os.path.join(output_folder, 'daily_charts_track_list.csv')
        track_list.to_csv(path, index=False)
        print(f'트랙 리스트 생성 성공 | 고유 곡 수: {len(track_list)}개')
        return track_list
    
    except Exception as e:
        print(f'트랙 리스트 생성 실패: {e}')

if __name__ == '__main__':
    load_track_list()