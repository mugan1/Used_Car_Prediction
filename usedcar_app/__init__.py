from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):

    app = Flask(__name__)

    # db 생성
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///used_car.sqlite3'

    if config is not None:
        app.config.update(config)

    # db 시작
    db.init_app(app)
    migrate.init_app(app, db)
    
    # bp 생성 
    from usedcar_app.views.main_page import main_bp
    from usedcar_app.views.dash_page import dash_bp
   
    app.register_blueprint(main_bp)
    app.register_blueprint(dash_bp)

    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)