from flask import Flask

def create_app():

    app = Flask(__name__)

    # @app.route('/')
    # def hello():
    #     return "Hello"
    
    from usedcar_app.views.main_page import main_bp
    from usedcar_app.views.dash_page import dash_bp
   
    app.register_blueprint(main_bp)
    app.register_blueprint(dash_bp, url_prefix='/dash')

    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)