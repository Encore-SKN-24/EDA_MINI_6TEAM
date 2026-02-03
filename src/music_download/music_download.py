from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import pandas as pd

music_df = pd.read_csv('././data/processed_data/daily_charts_track_list.csv')

def downloadYouTube(videourl, path, filename):
    yt = YouTube(videourl, on_progress_callback = on_progress)
    audio_stream = yt.streams.get_audio_only()
    
    # 다운로드
    audio_stream.download(output_path=path, filename=str(filename))

for i in music_df.iloc[1059:].itertuples(index=False):
    downloadYouTube(i.url, '././data/music/m4a', filename=f"{i.music_id}.m4a")