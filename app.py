from flask import Flask
from blueprints.info import info_bp
app = Flask(__name__)

app.register_blueprint(info_bp)

if __name__ == '__main__':
    app.run(debug=True)