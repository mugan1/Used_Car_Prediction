from flask import Blueprint, render_template
from flask import Blueprint, request, redirect, url_for, session, flash
from usedcar_app import db
from usedcar_app.models.input import Input
from lightgbm import LGBMRegressor
import numpy as np
import joblib

dash_bp = Blueprint('dash', __name__ , url_prefix='/sub')

@dash_bp.route('/', methods=['GET','POST'])
def second():

    return render_template('result.html')