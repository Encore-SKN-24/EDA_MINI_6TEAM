import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter 

df = pd.read_csv('../../data/processed_data/spotify_2025_daily_charts.csv', encoding='utf-8')
df['month'] = pd.to_datetime(df['date']).dt.month

# 계절 분리
seasons = {
    'Q1': [1, 2, 3],
    'Q2': [4, 5, 6], 
    'Q3': [7, 8, 9], 
    'Q4': [10, 11, 12], 
}

# 제목 정리
def clean_titles(text):
    return (
        text.astype(str)
        .str.replace(r'\(.*?feat.*?\)', '', regex=True)
        .str.replace(r'\(.*?with.*?\)', '', regex=True)
        .str.replace(r'-\s*feat.*$', '', regex=True)
        .str.replace(r'\(.*?Ver.*?\)', '', regex=True)
        .str.replace(r'\(.*?Intro.*?\)', '', regex=True)
        .str.strip()
    )

colormaps = {
    'Q1': 'twilight_shifted_r',
    'Q2': 'summer_r',
    'Q3': 'cool_r',
    'Q4': 'autumn_r'
}

for season, months in seasons.items():

    season_df = df[df['month'].isin(months)].copy()

    season_df['clean_title'] = clean_titles(season_df['track_name'])

    title_freq = Counter(season_df['clean_title'])
    
    wordcloud = WordCloud(
        font_path="C:/Windows/Fonts/malgun.ttf",
        background_color='white',
        colormap = colormaps[season],
        width=1000,
        height=1000,
        max_words=50
    ).generate_from_frequencies(title_freq)

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.title(season.capitalize())
    plt.axis('off')
    plt.savefig(f'{season}_wordcloud.png')
    plt.show()