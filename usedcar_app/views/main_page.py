from flask import Blueprint, render_template, request, redirect, url_for, flash
from usedcar_app import db
from usedcar_app.models.input import Input
from usedcar_app.models.car import Car
import joblib
import json
from csv import DictReader
from collections import Counter

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET','POST'])
def input() :

    # 페이지 접속시 GET으로 요청받음 -> 기본 시작 페이지
    if request.method == 'GET':
        return render_template('main.html')

    # 값을 입력하여 전송시 POST 방식
    else : 
        # request 값을 받음
        result = request.form
        try :
        # input order -> 연식, 주행거리, 연료, 배기량, 연비, 구동방식, 최대토크, 보험이력등록, 제조사, 마력, 보증여부
            year= float(result['year'])
            km= float(result['km'])
            fuel= float(result['fuel'])
            amount= float(result['amount'])
            ratio= float(result['ratio'])
            drive= float(result['drive'])
            torque= float(result['torque'])
            insurance= float(result['insurance'])
            factory= float(result['factory'])
            horse= float(result['horse'])
            guarantee= float(result['guarantee'])
        except :
            flash('입력은 숫자로! 옵션은 다 선택해주세요!')
            return redirect(url_for('main.input'))

        # model 호출 
        model = joblib.load('usedcar_app/utils/lightgbm.pickle')
        result_list = [year, km, fuel, amount, ratio, drive, torque, insurance, factory, horse, guarantee]
        predicted = model.predict([result_list])
        price = int(predicted[0])
        format_price = format(price, ',')

        # Input db 에 입력 
        inputtable=Input(year = year, km = km, fuel = fuel, amount = amount, ratio=ratio, drive=drive, torque=torque,
        insurance = insurance, factory=factory, horse=horse, guarantee=guarantee, price=price) 
        db.session.add(inputtable)
        db.session.commit()

        # model feature importance
        order_list = ['연식', '주행거리', '연료', '배기량', '연비', '구동방식', '최대토크', '보험이력등록', '제조사', '마력', '보증여부']
        features = model.feature_importances_
        s_features = sorted(features, reverse=True)
        s_features = [int(x) for x in s_features]
        # features 크기에 따라 orders 순서 변경
        orders = [list(features).index(x) for x in s_features]
        order_list = [order_list[i] for i in orders]

        feature_list = [order_list, s_features]

        # 사용자들의 input data price 호출 -> 평균값 계산 
        user_price = Input.query.filter(Input.price).all()
        mean_price = sum([u.price for u in user_price])//len([u.price for u in user_price])
        price_list = [price, mean_price, format_price]

        # 제조사, 연료, 구동방식 최빈값 
        inputtable = Input.query.filter().all()
        factory_dict={1:'쌍용', 2:'쉐보레', 3:'현대', 4:'기아', 5:'제네시스', 6:'르노삼성'}
        fuel_dict={1:'디젤', 2:'가솔린', 3:'LPG', 4:'하이브리드'}
        drive_dict={1:'4WD', 2:'전륜FF', 3:'후륜', 4:'AWD'}

        factory_mode = factory_dict[Counter([i.factory for i in inputtable]).most_common()[0][0]]
        fuel_mode = fuel_dict[Counter([i.factory for i in inputtable]).most_common()[0][0]]
        drive_mode = drive_dict[Counter([i.factory for i in inputtable]).most_common()[0][0]]
        cat_mode = [factory_mode, fuel_mode, drive_mode]
     
        # 예측결과(price)와 비슷한 가격대의 car db 호출 
        cartable = Car.query.filter((Car.price >= price-500000) & (Car.price <= price+500000)).all()

        return render_template('dash.html', price_list=price_list, feature_list=feature_list, cartable=cartable, cat_mode=cat_mode)

# csv 파일을 database에 넣기 위한 임시 코드 

# @main_bp.route('/import')
# def tmp() :
#     CSV_FILEPATH = 'usedcar_app/data/cars.csv'
#     with open(CSV_FILEPATH, newline='') as csvfile:
#         csv_file = DictReader(csvfile)
#         for row in csv_file:
#             car = Car(*row.values())
#             db.session.add(car)
#             db.session.commit()
#     db.session.close()
#     return "hi"







