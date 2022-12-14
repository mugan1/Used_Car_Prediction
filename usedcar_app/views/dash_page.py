from flask import Blueprint, render_template
from flask import Blueprint, request, redirect, url_for, session, flash
import joblib
from lightgbm import LGBMRegressor
import numpy as np
import pickle
dash_bp = Blueprint('dash', __name__ , url_prefix='/sub')

@dash_bp.route('/', methods=['GET','POST'])
def second():
    if request.method == 'GET' :
        result = {}
    else : 
        result = request.form
    
    # model = pickle.load(open('usedcar_app/utils/lgbm.pickle','rb'))
    model = joblib.load('usedcar_app/utils/lightgbm.pickle')
    # input_data = list(map(lambda x : int(x), result.values()))
    # a = np.array(input_data)
    x = model.predict([[1,1,1,1,1,1,1,1,1,1,1]])
    print(x)
    return render_template('result.html', result=result)