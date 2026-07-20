from flask import Flask, render_template
from config import Config


def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object(Config)

    @app.route("/")
    def home():
        return render_template("home/index.html")

    return app