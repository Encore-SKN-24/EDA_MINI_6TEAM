import pandas as pd
import os

def load_daily_charts():
    chart_list = []
    dates = pd.date_range(start='2025-01-01', end='2025-12-31').strftime('%Y-%m-%d')
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # 날짜별 차트 데이터 로드
        for date in dates:
            data_path = os.path.join(cur_dir, f'../../data/raw_data/regional-kr-daily-{date}.csv')
            df = pd.read_csv(data_path)
            
            # 날짜열 추가
            df['date'] = date
            chart_list.append(df)

        # 차트 통합
        chart_df = pd.concat(chart_list, axis=0, ignore_index=True)
        print('데일리 차트 통합 완료')
    
    except Exception as e:
        print('데일리 차트 통합 실패', e)

    try:
        # 통합 차트 저장
        output_folder = os.path.join(cur_dir, '../../data/processed_data')
        path = os.path.join(output_folder, 'spotify_2025_daily_charts.csv')
        chart_df.to_csv(path, index=False)
        print('통합 데일리 차트 저장 성공')
        return chart_df
    
    except Exception as e:
        print(f'통합 차트 저장 실패: {e}')

if __name__ == '__main__':
    load_daily_charts()