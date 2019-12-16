import os
import logging
from datetime import datetime as dt
from flask import Flask, request

from api import api
from config import config
from tools.flask_logs import LogSetup

ENV_CONFIG = "APP_CONFIGFILE"
CONFIG_NAME = os.environ.get("FLASK_ENV") or "development"

app = Flask(__name__)

if os.environ.get(ENV_CONFIG):
    app.config.from_envvar(ENV_CONFIG, silent=False)
else :
    app.config.from_object(config[CONFIG_NAME])

api.init_app(app)

logs = LogSetup()
logs.init_app(app)

@app.after_request
def after_request(response):
    """ Logging after every request. """
    logger = logging.getLogger("app.access")
    logger.info(
        "%s [%s] %s %s %s %s %s %s %s",
        request.remote_addr,
        dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
        request.method,
        request.path,
        request.scheme,
        response.status,
        response.content_length,
        request.referrer,
        request.user_agent,
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)
