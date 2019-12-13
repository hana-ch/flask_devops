import os
from flask import Flask

from api import api
from config import config

ENV_CONFIG = "APP_CONFIGFILE"
CONFIG_NAME = os.environ.get("FLASK_ENV") or "development"

app = Flask(__name__)

app.config.from_envvar(ENV_CONFIG, silent=True)
app.config.from_object(config[CONFIG_NAME])


api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
