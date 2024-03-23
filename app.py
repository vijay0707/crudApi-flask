from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from config.settings import Config
from api.controllers import *

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
swagger = Swagger(app, template_file='swagger/crud_template.yml')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
