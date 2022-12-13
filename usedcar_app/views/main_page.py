from flask import Blueprint
from usedcar_app.models.user import User
from usedcar_app.models.member import Member

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index() :
    user_list = User.query.all()
    mem_list = Member.query.all()
    return "hi"