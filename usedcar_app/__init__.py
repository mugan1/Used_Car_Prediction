from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import joblib
from dotenv import load_dotenv
from sqlalchemy import MetaData
import os
import config

load_dotenv()
db = SQLAlchemy()
migrate = Migrate()
DATABASE_URI = os.getenv("DATABASE_URI")

def create_app(config=None):

    app = Flask(__name__)
    
    # db 생성

    # app 배포시 
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # 배포하지 않을때 
    # if app.config["ENV"] == 'production':
    #    app.config.from_object('config.ProductionConfig')
    # else:
    #    app.config.from_object('config.DevelopmentConfig')

    # flash를 위한 secret key 생성
    app.config["SECRET_KEY"] = "ABCD"

    if config is not None:
        app.config.update(config)

    # db 시작
    db.init_app(app)
    migrate.init_app(app, db)
    
    # bp 생성 
    from usedcar_app.views.main_page import main_bp
   
    app.register_blueprint(main_bp)

    return app
    
if __name__ == "__main__":
    app = create_app()
    
    app.run(debug=True)