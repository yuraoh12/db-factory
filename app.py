from flask import Flask
import config


def create_app() :
    
    app = Flask(__name__)
    app.config.from_object(config)
    import views.test_view as test_view

    app.register_blueprint()

    @app.route('/')
    def test_view() :
        return '123123'