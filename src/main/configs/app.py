from flask import Flask
from flask_cors import CORS
from src.main.routes import api_routes_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_routes_bp)


# @app.route("/users")
# def hello_world():
#     return "<p>Hello World</p>"
