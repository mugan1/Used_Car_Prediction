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
(https://www.notion.so/Used-Car-Price-Prediction-bd62a454e9774ce2a8c72cedd56350dc?pvs=4#6132cb9fbd7241c4a159cd023c0caf9a)




### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc



[Project Portfolio Link] (https://www.notion.so/Used-Car-Price-Prediction-bd62a454e9774ce2a8c72cedd56350dc)

[웹 애플리케이션 주소] (https://usedcar-haebing25.koyeb.app/)
