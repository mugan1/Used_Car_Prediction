# Project Title

중고차 예측 웹 어플리케이션 프로젝트 

## Overview

- 기간  |  2021. 08 ~ 2021. 09
- 담당 파트 |  개인프로젝트
- 플랫폼 |  Python, Colab, FLASK

### Background & Goal

원하는 스펙의 중고차 적정 가격을 예측하고, 결과에 관련된 분석 데이터를 대시보드로 출력할 수 있는 웹 애플리케이션을 제작/배포하고자 계획함
- 웹 스크래핑을 통해 중고차 데이터 확보
- 중고차 가격 예측 ML 모델 구현 및 성능 확인 
- FLASK를 사용하여 대시보드 애플리케이션 개발 

### Dataset

- 보배드림 [Link](https://www.bobaedream.co.kr/) 에서 웹스크래핑을 통해 데이터 확보(코드 : 깃허브 내 webscrapping.py)
- 데이터 Preprocessing 및 EDA 관련 코드 깃허브 colab파일로 업로드

## Data Features

```
1. Data Shape : 1541 rows, 24 columns
2. 웹스크래핑을 통해 수집한 Features 
- 이름 : 중고차 모델명
- 가격 : 중고차 매물 가격
- 연식 : 개월수로 전처리 후 표기
- 주행거리 : km 단위
- 연료 : 디젤, 가솔린, LPG, 하이브리드
- 배기량 : 실린더의 총 용량 / cc단위
- 색상 : 중고차 색상
- 엔진형식 : 중고차의 엔진 사양 상세
- 연비 : km/ℓ 단위
- 구동방식 : 4WD(4륜구동), 전륜, 후륜, AWD(전륜구동)
- 중량 : kg 단위
- 최대토크 : 순간적으로 낼 수 있는 힘 / kg.m 단위
- 보험이력등록 : 보험이력등록 여부(등록/미등록)
- 소유자변경 : 중고차 소유자 변경 횟수
- 전손 : 중고차 전체 소실, 파손 횟수
- 침수전손 : 침수로 인한 중고차 전체 소실, 파손 횟수
- 침수분손 : 침수로 인한 중고차 일부 소실, 파손 횟수
- 도난 : 중고차 도난 횟수
- 내차피해(횟수) : 중고차 피해 횟수
- 내차피해(가격) : 중고차 피해 가격 총액
- 타차가해(횟수) : 타차 가해 횟수 
- 타차가해(가격) : 타차 가해 가격 총액
- 제조사 : 현대/기아/쉐보레/제네시스/쌍용/르노삼성
- 마력 : 내연 기관 일률 단위
- 보증여부 : 보증여부(보증/미보증)
- 보증기간 : 보증기간 개월 단위
- 보증거리 : 보증거리 km 단위

```

### Data Preprocessing

1. Feature 제거
    - 침수전손, 침수전손, 도난의 경우 대부분의 value가 0 : Feature 삭제
2. 이상치 제거
<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/4c887399-6d01-4d6d-a0de-be736d691ddd" alt="text" width="number" />
  <br> 이상치 제거 전 Boxplot
</p>

선형회귀분석에서 가격, 연식, 주행거리 변수의 이상치가 MAE를 높이는 것으로 확인함 : 위의 세 변수에 대한 이상치를 IQR(Inter Quantile Range)방식으로 제거 

<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/89d2ec08-778e-48db-b840-33f5859a315b" alt="text" width="number" />
  <br> 이상치 제거 후 세 변수에 대한 Boxplot
</p>


### EDA

1. 가격에 대한 Distplot

<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/c4c5dc5c-ad90-41eb-92b7-c2e4857f649b" alt="text" width="number" />
  <br> 우측으로 긴 꼬리를 가진 가격 분포
</p>

2. 연속형 변수 간 상관관계 
<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/2f2665b2-0e28-4604-985e-11013b9723ed" alt="text" width="number" />
  <br> 우측으로 긴 꼬리를 가진 가격 분포
</p>

  - 가격과 상관관계가 높은 변수는 연식, 주행거리가 음의 상관관계, 중량과 마력이 양의 상관관계를 가지고 있음 
  - 연식과 주행거리, 배기량과 마력 등이 높은 상관성을 지니고 있음. 다중공선성 문제가 발생할 수 있지만, 특성상호작용 문제를 잘 해결할 수 있는 트리 모델을 사용할 것이기 때문에 특성상호작용에 대해서는 고려하지 않기로 함

3. 범주형 변수 간 상관관계
<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/67857d7c-7f1c-4bc5-b068-6d84d5747afc" alt="text" width="number" />
</p>

  - 가격과 범주형 변수간의 관계에서는 하이브리드 연료, 전륜 구동방식, 제네시스 제조사, 보증 가능, 보험이력 등록이 높은 가격을 형성하는 데에 영향을 미치는 것으로 확인됨
  - 중고차 이름, 엔진형식, 색상의 경우 높은 cardinality로 모델의 성능을 떨어뜨릴 것으로 판단하며, 웹 애플리케이션에서 입력받기도 힘든 변수이기 때문에 활용 변수에서 삭제하기로 함 

   
## Modeling(1차)

1차 모델 중 가장 좋은 성능을 보인 LightGBM을 최종 모델로 선택

1. 기준모델(훈련 데이터 가격 평균) MAE : 8390594
2. Linear Regression MAE : 3924783
3. LightGBM Regressior MAE : 3102346

## Feature Selection

사용자 입력화면에서 받을 데이터 수를 줄여야할 필요성이 있으므로 sklearn의 Select K-Best을 사용하여 주요 변수를 11개만 추출
- Select K-Best : Feature Selection의 일종으로 Target 변수와의 상관관계를 계산하여 가장 중요하다고 판단되는 변수를 K개 산출하는 방식
- 선택된 최종 변수 : 연식, 주행거리, 연료, 배기량, 마력, 최대토크, 제조사, 보증여부, 보험이력등록, 구동방식, 연비
  
## LightGBM Modeling

최종 모델인 LightGBM을 사용하여 최적화된 예측 결과를 찾아낼 예정
- lightGBM : Gradient Boosting 모델 중 연산 속도가 빨라 웹 애플리케이션에 탑재하기 편리함
- Gradient Boosting : 앙상블 알고리즘의 일종으로, Gradient(잔차)를 이용하여 이전 모형의 약점을 보완하는 새로운 모형을 순차적으로 적합한 뒤, 이들을 선형결합하여 얻어진 모형을 생성하는 지도학습 알고리즘 
- RandomizedsearchCV : 최적화된 하이퍼파라미터를 찾는 메소드 

## Result

훈련데이터 MAE:  4902909 / R2 Score : 0.56
검증데이터 MAE:  5567629 / R2 Score : 0.42
테스트데이터 MAE:  4893349 / R2 Score : 0.64
- 데이터량의 부족과 11개의 변수만을 사용했기 때문에 모델의 성능이 많이 떨어짐. 추후 데이터 추가 확보와 최적화 과정을 통해 모델의 성능을 올릴 예정

## XAI

1.예측가격과 실제 가격의 차

<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/e4cc2822-e1e1-4136-a96d-77c34a029d2b" alt="text" width="number" />
    <br>가격대가 높을수록 오차가 크게 나타나는 것을 확인할 수 있음
</p>
    
2. Feature Importance : 각각 특성을 모든 트리에 대해 평균불순도감소를 계산하는 방식
   
<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/ffaecaa3-bd8b-4e85-9405-b83d93a2aed6" alt="text" width="number" />
</p>

3. Permutation Importance : 관심있는 특성에만 무작위로 노이즈를 주고 예측을 하였을 때 성능 평가지표가 얼마나 감소하는 지 측정하는 방식

<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/38e14078-4f8b-425b-bbe3-a1ad345fa789" alt="text" width="number" /><br>
</p>
- 두 방식을 통해 연식, 주행거리, 마력, 배기량, 연비, 최대토크 정도가 모델 예측에 주요 변수로 작용하는 것을 확인
- 데이터량의 부족과 11개의 변수만을 사용했기 때문에 모델의 성능이 많이 떨어짐. 추후 데이터 추가 확보와 최적화 과정을 통해 모델의 성능을 올릴 예정    

4. SHAP
   
<p align="center">
  <img src="https://github.com/mugan1/Used_Car_Prediction/assets/71809159/b372c7a2-a773-4efb-9426-6e6a5ce795b3" alt="text" width="number" /><br>
</p> 
- 테스트 10번 인덱스 데이터의 경우 주행거리, 배기량, 보험이력등록여부가 가격을 높이는 요인이며, 연식, 최대토크, 마력, 연료가 가격 낮추는 요인으로 작용함을 알 수 있음




[Project Portfolio Link] (https://www.notion.so/Used-Car-Price-Prediction-bd62a454e9774ce2a8c72cedd56350dc)

[웹 애플리케이션 주소] (https://usedcar-haebing25.koyeb.app/)
