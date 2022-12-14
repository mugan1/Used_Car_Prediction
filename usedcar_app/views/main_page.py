from flask import Blueprint, render_template
from usedcar_app import db
from usedcar_app.models.input import Input
from usedcar_app.models.car import Car
from csv import DictReader

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index() :
    return render_template('main.html')

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







