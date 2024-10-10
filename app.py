from flask import Flask
from repository.csv_repository import init_db
from blueprints.info import info_bp
app = Flask(__name__)

app.register_blueprint(info_bp)
# @app.route('/')
# def init():
#     init_db()
#     return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)