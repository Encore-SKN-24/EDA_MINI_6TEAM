import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

music_df = pd.read_csv('././data/processed_data/daily_charts_analyze.csv')
music_df = music_df.drop(['url'], axis=1)
for i in range(len(music_df)):
    # 오디오 파일 로드
    y, sr = librosa.load(f'././data/music/mp3/{music_df['music_id'].iloc[i]}.mp3')  # 오디오 파일 로드

    # tempo
    # 템포를 얻기 위해선 beat가 필요함
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    tempo = round(tempo[0], 2)
    music_df.at[i, 'tempo'] = tempo

    # mel : 사람 귀가 느끼는 실제 에너지
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)

    # 데시벨 단위로 변환 0db가 최대
    S_dB = librosa.power_to_db(S, ref=np.max)
    mean_mel = np.mean(S_dB)
    music_df.at[i, 'mean_mel'] = round(mean_mel, 2)

    # rms : 언제 소리가 진폭되는지 알 수 있음
    rms = librosa.feature.rms(y=y)
    times = librosa.times_like(rms)

    mean_rms = np.mean(rms)
    max_rms = np.max(rms)
    music_df.at[i, 'mean_rms'] = float(round(mean_rms, 4))
    music_df.at[i, 'max_rms'] = float(round(max_rms, 4))

    # zero_crossing_rate : 얼마나 거칠고 공격적인지
    zero = librosa.feature.zero_crossing_rate(y)
    times = librosa.times_like(zero)

    # 전체 곡의 평균 거칠기 계산
    mean_zcr = np.mean(zero)
    music_df.at[i, 'mean_zcr'] = float(round(mean_zcr, 4))

    # 거칠기의 변화 정도 (값이 들쭉날쭉하면 곡의 전개가 다이나믹함)
    std_zcr = round(np.std(zero), 2)
    music_df.at[i, 'std_zcr'] = std_zcr

    # spec_centroid : 소리의 밝기 정도
    spec_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

    # 시간대 별로 평균
    mean_centroid = np.mean(spec_centroid)
    music_df.at[i, 'mean_centroid'] = round(mean_centroid, 2)

music_df.to_csv('././data/processed_data/daily_charts_analyze.csv', index=False)