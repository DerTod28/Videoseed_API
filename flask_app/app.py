from flask import Flask
from blueprint import bp, swaggerui_blueprint

app = Flask(__name__)
app.register_blueprint(bp)

app.register_blueprint(swaggerui_blueprint)


if __name__ == '__main__':
    app.run()
