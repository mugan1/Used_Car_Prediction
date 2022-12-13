from flask import Blueprint

dash_bp = Blueprint('dash', __name__)

@dash_bp.route('/')
def second():
    return 'Dash'