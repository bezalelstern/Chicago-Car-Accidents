from flask import Flask
from repository.csv_repository import init_db
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    init_db()
    app.run(debug=True)