from flask import Blueprint, render_template
from usedcar_app.models.user import User
from usedcar_app.models.member import Member

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index() :
    return render_template('main.html')