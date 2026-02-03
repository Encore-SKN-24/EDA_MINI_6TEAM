from pydub import AudioSegment
import pandas as pd

# 오디오파일 불러오기
for i in range(1126, 1129):
    audio = AudioSegment.from_file(f'././data/music/m4a/{i}.m4a', format="m4a")
    audio.export(f"././data/music/mp3/{i}.mp3", format="mp3")
