from flask import Blueprint, render_template
from flask import Blueprint, request, redirect, url_for, session, flash

dash_bp = Blueprint('dash', __name__ , url_prefix='/sub')

@dash_bp.route('/', methods=['GET','POST'])
def second():

    return render_template('index.html')