import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# beautifulsoup 객체를 불러오는 함수

def get_soup(url):
    res = requests.get(url, verify=False)
    res.raise_for_status()
    requests.adapters.DEFAULT_RETRIES = 10
    soup = BeautifulSoup(res.text,"lxml")
    return soup

cols = ['이름','가격', '신차대비', '연식', '주행거리', '연료', '배기량', '색상', '보증정보', '엔진형식', '연비', '구동방식', '중량', '최대토크',
"보험이력등록","소유자변경","전손","침수전손","침수분손","도난","내차피해(횟수)","내차피해(가격)","타차가해(횟수)","타차피해(가격)"]
df_cars= []
pagenum = 100
for i in range(1, pagenum+1) :
    url = "http://www.bobaedream.co.kr/cyber/CyberCar.php?refer_page=%2Fcyber%2FCyberCar.php&gubun=K&order=S11&view_size=50&search_cat=C3&search_cat_gubun=s0&search_field=car_name&view_stat=0&page="+str(i)
    # res=requests.get(url, verify=False)
    # res.raise_for_status()
    # requests.adapters.DEFAULT_RETRIES = 10
    # soup=BeautifulSoup(res.text,"lxml")

    # soup 객체 호출 
    soup = get_soup(url)
    # product-item class의 모든 li 부르기
    cars=soup.find_all("li",attrs={"class":"product-item"})

    # 1페이지 내 있는 자동차 목록의 링크(페이지 당 50개)

    for car in cars:
        link = "https://www.bobaedream.co.kr" + car.a["href"]
        # 세부 페이지 soup 호출
        soup_detail = get_soup(link)
        # try:
        #   res2=requests.get(link, verify=False)
        #   res2.raise_for_status()
        #   requests.adapters.DEFAULT_RETRIES = 10
        #   soup_detail = BeautifulSoup(res2.text, "lxml")
        # except requests.exceptions.ConnectionError:
        #   res2.status_code = "Connection refused"
       
        # 차량 이름과 가격 
        name=soup_detail.find("h3",{"class":"tit"}).get_text()
        price = soup_detail.find("span",{"class":"price"}).get_text()

        # 신차 가격 비 구하기(준비중인 경우 가격비 ''으로 설정)
        infobox = soup_detail.find("div", attrs={"class": "info-util box"})
        try:
            ratio = infobox.find("b").get_text()
        except:
            ratio = ''

        # 상세페이지 기본 정보 
        basic = soup_detail.find("div", {"class" : "info-basic"})
        year = basic.find("th", text="연식").find_next().get_text()
        km = basic.find("th", text="주행거리").find_next().get_text()
        fuel = basic.find("th", text="연료").find_next().get_text()
        amount = basic.find("th", text="배기량").find_next().get_text()
        color = basic.find("th", text="색상").find_next().get_text()
        guar = basic.find("b",text='보증정보').find_next("td").get_text()

        # 차량제원

        form = soup_detail.find("span", text="엔진 형식").find_next().get_text()
        effi = soup_detail.find("span", text="연비").find_next().get_text()
        method = soup_detail.find("span", text="구동방식").find_next().get_text()
        weight = soup_detail.find("span", text="차량중량").find_next().get_text()
        torque = soup_detail.find("span", text="최대토크").find_next().get_text()

        #보험이력을 등록했을 경우 보험 관련정보
        #보험관련정보가 없을 경우 오류가 나므로 try/except 처리 
        if soup_detail.find("div", {"class" : "info-util box"}).find("i").find("em")==None :
            acc1 = '미등록'
        else:
            acc1 = '등록'
		
        findacci_info1=[]
        try:
            if acc1=='등록':
                acc1table=soup_detail.find("div",attrs={"class":"info-insurance"})
                insurdt1=acc1table.find("th",text="차량번호/소유자변경").find_next().get_text()[-2]
                insuraccis1 = acc1table.find("th", text="자동차보험 특수사고").find_next().get_text().split('/')
                insurdt2=insuraccis1[0][-2]
                insurdt3 = insuraccis1[1][-2]
                insurdt4 = insuraccis1[2][-2]
                insurdt5 = insuraccis1[3][-1]
                insuraccis2=acc1table.find("th", text="보험사고(내차피해)").find_next().get_text().split('회')
                insurdt6=insuraccis2[0]
                insurdt7=insuraccis2[1][2:-2]
                insuraccis3=acc1table.find("th", text="보험사고(타차가해)").find_next().get_text().split('회')
                insurdt8=insuraccis3[0]
                insurdt9=insuraccis3[1][2:-2]
                findacci_info1=[insurdt1,insurdt2,insurdt3,insurdt4,insurdt5,insurdt6,insurdt7,insurdt8,insurdt9]
            else:
                findacci_info1=['']*9
        except :
                findacci_info1 = ['']*9
        temp = [name, price, ratio, year, km, fuel, amount, color, guar, form, effi, method, weight, torque] + [acc1] + findacci_info1
        df_cars.append(temp)

    # 1 page 당 임시적으로 dataframe 생성 후 저장
    df_tmp = pd.DataFrame(data=df_cars, columns=cols)
    df_tmp.to_csv(f'{i}_tmp_cars.csv')
    print(f'{i} page complete')

# 결과 저장
df_total=pd.DataFrame(data=df_cars,columns=cols) 
df_total.to_csv('cars.csv')