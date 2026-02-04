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

## 🎵 음악 선택에 영향을 주는 요소 탐색

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
![wbs](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/wbs.png)
---

## 데이터 수집

### **출처**

- Spotify https://www.spotify.com/kr-ko/premium/
- iTunes Search API
```
GET | https://itunes.apple.com/search?term={query}&entity=song&limit=1
```
- YouTube https://www.youtube.com
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
<a href="https://librosa.org/doc/latest/index.html">
  <img width="320" height="131" alt="image" src="https://github.com/user-attachments/assets/1fc2d478-0768-49d3-a07e-fb46c750d3ba" />
</a>

### 오디오 신호를 분석해 음향 특징을 추출하는 파이썬 라이브러리이다.
<a href="https://github.com/pytube/pytube">
  <img width="456" height="143" alt="image" src="https://github.com/user-attachments/assets/ccfe0d00-9c56-4bd7-a28c-29ee76c71410" />
</a>

### YouTube 영상을 다운로드할 수 있게 하는 라이브러리이다.

---

## 그래프로 상관관계 분석
### 곡의 음향 특징과 날씨의 상관관계
![weather](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/w_heatmap.png)
### 템포와 temp_avg(기온 평균), DI(불쾌지수)는 음의 상관관계를 가진다.
### DI(불쾌지수)과 temp_avg(기온 평균)은 각각 mean_mel(에너지 평균), mean_zcr(거칠기 평균), mean_centroid(밝기 평균)와 양의 상관관계를 가진다.

### 기온과 템포의 상관관계
![temp2](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/tempo.png)
![temp](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/t_heatmap.png)
### 기온과 템포는 역의 추세가 보인다.

### 계절별 키워드와 스트리밍 수의 상관관계
![spring](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/k_spring.png)
```
'봄', 'spring', '벚꽃', 'blossom'
```
### 벚꽃시즌일 때 키워드와 관련된 스트리밍 수가 증가했다.

![summer](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/k_summer.png)
```
'summer', '여름', '바다', 'cool', '시원'
```
### 여름의 키워드가 국한되지 않기 때문에 유의미한 상관관계가 없었다.

![winter](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/k_winter.png)
```
christmas', '크리스마스', 'snow', '눈
```
### 크리스마스가 있어 키워드와 관련된 스트리밍 수가 증가했다.

### 음악 밝기 수와 기온의 상관관계

![bright](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/Brightness.png)
### 여름 시기에 음악 밝기 수가 증가했다.
---
## 분기별 인기 있었던 노래 제목
### 1분기 (1월 ~ 3월)
![q1](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/Q1_wordcloud.png)
### 2분기 (4월 ~ 6월)
![q2](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/Q2_wordcloud.png)
### 3분기 (7월 ~ 9월)
![q3](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/Q3_wordcloud.png)
### 4분기 (10월 ~ 12월)
![q4](https://github.com/Encore-SKN-24/EDA_MINI_6TEAM/blob/main/README%20images/Q4_wordcloud.png)
---
## 결론 
### 음악선택에 영향을 주는 요소들은 계절, 기온과 관련이 있다는 걸을 확인했습니다.
---
## 회고록
- `김현수`</br>

- `류지우` </br>
라이브러리를 활용해 다양한 음향 특성을 추출하며 많은 데이터를 분석할 수 있었고 이 과정에서 실제 상관관계를 증명하는 과정이 재미있었다.  
다만 스포티파이와 iTunes에서 가져온 곡 제목과 아티스트가 영어로 되어 있고 장르가 세분화되어 있지 않아 다양하고 밀접한 연관성을 충분히 뽑아내지 못한 점은 아쉬웠다.
- `조아름`</br>
  차트인 트랙리스트에 iTunes Search API를 활용하여 장르, 발매 국가, 곡 길이 데이터를 수집하는 역할을 맡았는데 요청 제한으로 인해 시간이 예상보다 오래 걸렸고 코드 수정에도 어려움이 있었습니다. 근데 모든 데이터를 수집하고난 뒤 발매 국가가 대부분 USA로 동일하게 제공되고 장르 또한 세분화되어 있지 않아 분석에 활용하기 어렵다는 한계를 확인하였고, 이를 통해 외부 API 데이터의 품질과 한계를 직접 경험할 수 있었습니다. 비록 해당 데이터는 사용하지 못했지만, 계절별 키워드 분석에서 의미 있는 결과를 도출하여 프로젝트 전반에 기여할 수 있었던 것 같아 만족스러웠습니다.

- `진세형`</br>

- `최현진`</br>
개인 일정으로 프로젝트 기간에 적극적으로 참여하지 못해 아쉬웠습니다.
최종 결과물을 보면서 음악의 템포를 활용하고
차트 데이터를 날씨나 계절 같은 환경 요인과 연관 지어 분석한다는 접근이 흥미로웠으며,
실제로 일부 영향이 있다는 점이 인상적이었습니다.

