from flask import Blueprint, render_template, request, redirect, url_for, flash
from usedcar_app import db
from usedcar_app.models.input import Input
import joblib
from csv import DictReader

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
        #numeric type이 들어오지 않았을 시
        for value in result.values() :
            if value.isnumeric() == False:
                flash('입력은 숫자로! 옵션은 다 선택해주세요!')
                return redirect(url_for('main.input'))

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

        # Input db 에 입력 
        inputtable=Input(year = year, km = km, fuel = fuel, amount = amount, ratio=ratio, drive=drive, torque=torque,
        insurance = insurance, factory=factory, horse=horse, guarantee=guarantee) 
        db.session.add(inputtable)
        db.session.commit()
        db.session.close()

        # model 호출 

        model = joblib.load('usedcar_app/utils/lightgbm.pickle')
        result_list = [year, km, fuel, amount, ratio, drive, torque, insurance, factory, horse, guarantee]
        predicted = model.predict([result_list])
        
        return render_template('result.html', predicted=predicted, result=result)

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







