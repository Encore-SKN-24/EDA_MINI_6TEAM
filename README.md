# SKN24_EDA_MINI_6TEAM

## 🍦 TEAM I-스크림

> _“발표는 조용히, 분석은 집요하게”_

**TEAM I-스크림**은  
모든 팀원이 MBTI `I`로 구성된 팀으로,  
조용하지만 집요하게 데이터를 파고드는 성향을 가지고 있습니다.

<!-- prettier-ignore-start -->
|김현수|류지우|조아름|진세형|최현진|
| :--: | :--: | :--: | :--: | :--: |
| [![github - BarryKim34](https://img.shields.io/badge/BarryKim34-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BarryKim34) | [![github - jia11234](https://img.shields.io/badge/jia11234-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jia11234) | [![github - areum117](https://img.shields.io/badge/areum117-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/areum117) | [![github - gugu_eightyone](https://img.shields.io/badge/gugu_eightyone-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gugu-eightyone) | [![github - lifeisgoodlg](https://img.shields.io/badge/junhaj27-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lifeisgoodlg) |
<!-- prettier-ignore-end -->

## 노래 선택에 영향을 주는 요소 탐색

### 주제 선정 이유

일반적으로 음원 차트 성과는  
아이돌 팬덤의 집중 스트리밍, 즉 *줄세우기 문화*의 영향을 크게 받는다고 알려져 있습니다.  
그러나 이러한 요인을 제외했을 때에도,

- 노래의 **음악적 특성**
- **계절·날씨와 같은 외부 환경**

이 실제 음악 소비와 차트 진입에  
어떤 영향을 미치는지에 대한 분석은 상대적으로 부족합니다.

이에 본 프로젝트에서는  
차트 데이터를 단순 순위가 아닌  
**그 시기의 분위기와 선택의 결과**로 바라보고,  
데이터를 통해 이를 탐색하고자 했습니다.

### 필요성

음악은 일상과 밀접한 콘텐츠로,  
사람들의 감정 상태나 외부 환경에 따라  
자연스럽게 소비 패턴이 달라질 수 있지 않을까 생각했습니다.

특히,

- 계절 변화
- 기온
- 날씨 상태

와 같은 요소는  
노래의 분위기나 템포 선호에 영향을 줄 가능성이 있다고 생각했습니다.

본 프로젝트는 다음과 같은 점에서 의미를 가집니다.

- 차트 분석을 **팬덤 중심 시각에서 확장**
- 음악의 **속성과 환경 요인 간 관계를 데이터로 확인**
- 상관관계 중심의 EDA를 통해  
  차트 소비의 숨겨진 흐름 탐색

---

## 데이터 수집

### **출처**

- Spotify
- iTunes Search API
- 기상청데이터 https://www.weatheri.co.kr/

### Spotify 일별 차트

- 수집 범위 : 2025년 1월 1일 ~ 2025년 12월 31일
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

- 2025년에 차트에 있었던 음원들 상세 정보 추가
- 수집 데이터

| 컬럼명           | 설명        |
| :--------------- | :---------- |
| genre            | 장르        |
| track_length_sec | 곡 길이(ms) |
| release_country  | 발매 국가   |

### 파이썬 라이브러리?

- 여기 추가 해주세요

... (184줄 남음)
