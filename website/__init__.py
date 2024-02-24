from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Praudexai_Tech'

    from .views import views

    app.register_blueprint(views)  # Remove the url_prefix parameter

    return app
