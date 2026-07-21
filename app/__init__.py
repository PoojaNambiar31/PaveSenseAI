from flask import Flask
from config import Config

from app.routes.home import home
from app.routes.complaint import complaint
from app.routes.auth import auth
from app.routes.dashboard import dashboard
from app.routes.profile import profile

def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(home)
    app.register_blueprint(complaint)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(profile)

    return app