# SKN24_EDA_MINI_6TEAM

## 🍦 TEAM I-스크림

**TEAM I-스크림**은  
모든 팀원이 MBTI `I`로 구성된 팀으로,  
조용하지만 집요하게 데이터를 파고드는 성향을 가지고 있습니다.

<!-- prettier-ignore-start -->
|김현수|류지우|조아름|진세형|최현진|
| :--: | :--: | :--: | :--: | :--: |
| [![github - BarryKim34](https://img.shields.io/badge/BarryKim34-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BarryKim34) | [![github - jia11234](https://img.shields.io/badge/jia11234-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jia11234) | [![github - areum117](https://img.shields.io/badge/areum117-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/areum117) | [![github - gugu_eightyone](https://img.shields.io/badge/gugu_eightyone-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gugu-eightyone) | [![github - lifeisgoodlg](https://img.shields.io/badge/lifeisgoodlg-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lifeisgoodlg) |
<!-- prettier-ignore-end -->

## 🎵음악 선택에 영향을 주는 요소 탐색

### 주제 선정 이유
- **음악적 특성**
- **계절·날씨와 같은 외부 환경**

본 프로젝트에서는  
차트 데이터를 단순 순위가 아닌  
**그 시기의 분위기 선택의 결과**로 바라보고,  
데이터를 통해 이를 탐색하고자 했습니다.

### 필요성

음악은 일상과 밀접한 콘텐츠로,  
사람들의 감정 상태나 외부 환경에 따라  
자연스럽게 음악 선택이 달라질 수 있지 않을까 생각했습니다.

특히,

- 계절 변화
- 기온
- 날씨 상태

와 같은 요소는  
음악의 분위기나 템포 선호에 영향을 줄 가능성이 있다고 생각했습니다.

본 프로젝트는 다음과 같은 점에서 의미를 가집니다.

- 차트 분석을 **다양한 시각으로 확장**
- 음악의 **속성과 환경 요인 간 관계를 데이터로 확인**

---

## WBS
- 이미지 넣기
---

## 데이터 수집

### **출처**

- Spotify
- iTunes Search API
```
GET | https://itunes.apple.com/search?term={query}&entity=song&limit=1
```
- Youtube
- 날씨데이터 https://www.weatheri.co.kr/

### Spotify 일별 차트

- 수집 범위 : 2025년 1월 1일 ~ 2025년 12월 31일
- spotify_2025_daily_charts.csv
- 수집 데이터
  
| 컬럼명        | 설명        |
| :------------ | :---------- |
| rank          | 순위        |
| uri           | URI         |
| artist_names  | 아티스트명  |
| track_name    | 곡명        |
| source        | 발매회사    |
| peak_rank     | 최고 순위   |
| previous_rank | 이전 순위   |
| days_on_chart | 차트인 기간 |
| streams       | 스트리밍 수 |
| date          | 날짜        |

### 음원 상세 정보 (iTunes)

- 2025년에 차트에 있었던 음원들 상세 정보 및 음향 특징 추가
- merged_music.csv
- 수집 데이터
  
| 컬럼명           | 설명 |
| :--------------- | :--- |
| genre            | 장르 |
| track_length_sec | 곡 길이(ms) |
| release_country  | 발매 국가 |
| tempo            | 템포 |
| mean_mel         | 사람 귀 기준으로 변환한 주파수 에너지 평균 |
| mean_rms         | 평균 음량 |
| max_rms          | 최대 음량 |
| mean_zcr         | 소리의 거칠기 평균 |
| std_zcr          | 거칠기 변화 정도 |
| mean_centroid    | 음악의 밝기 평균 |

---

## 파이썬 라이브러리
<img width="320" height="131" alt="image" src="https://github.com/user-attachments/assets/1fc2d478-0768-49d3-a07e-fb46c750d3ba" />

### 오디오 신호를 분석해 (숫자데이터)음향 특징을 추출하는 파이썬 라이브러리다.
<img width="456" height="143" alt="image" src="https://github.com/user-attachments/assets/ccfe0d00-9c56-4bd7-a28c-29ee76c71410" />

### YouTube 영상을 다운로드할 수 있게 하는 라이브러리이다.(에프에프엠펙)

---

## 그래프로 상관관계 분석
### 곡의 음향 특징과 날씨의 상관관계
이미지 넣기
### 가장 연관이 없는 것은 템포와 temp_avg(기온 평균), DI(불쾌지수)이다.
### 가장 연관이 있는 것은 DI(불쾨지수)과 temp_avg(기온 평균)은 각각 mean_mel(에너지 평균), mean_zcr(거칠기 평균), mean_centroid(밝기 평균)이다.

### 기온과 템포의 상관관계
이미지 넣기 2개
### 기온과 템포는 역의 추세가 보인다.

### 계절별 키워드와 스트리밍 수의 상관관계
봄
```
'봄', 'spring', '벚꽃', 'blossom'
```
### 벚꽃시즌일 때 키워드와 관련된 스트리밍 수가 증가했다.
여름
```
'summer', '여름', '바다', 'cool', '시원'
```
### 여름의 키워드가 국한되지 않기 때문에 유의미한 상관관계가 없었다.
겨울
```
christmas', '크리스마스', 'snow', '눈
```
### 크리스마스가 있어 키워드와 관련된 스트리밍수가 증가헀다.

### 음악 밝기 수와 온도의 상관관계
이미지
### 여름 시기에 음악 밝기 수가 증가했다.

### 분기별 인기있었던 노래 제목
### 1분기 (1월 ~ 3월)
이미지
### 2분기 (4월 ~ 6월)
이미지
### 3분기 (7월 ~ 9월)
이미지
### 4분기 (10월 ~ 12월)
이미지
