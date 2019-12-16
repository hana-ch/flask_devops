import os
import logging
from datetime import datetime as dt
from flask import Flask, request

from api import api
from config import config
from tools import logs
from models import db

ENV_CONFIG = "APP_CONFIGFILE"


# config_name : development | testing | production | default 
def create_app(config_name="development", config_file="config.cfg"):

    app = Flask(__name__, static_folder="static", template_folder="templates")

    # If env variable is set, use config file 
    # Else use configuration from config_name
    if os.environ.get(ENV_CONFIG):
        app.config.from_envvar(ENV_CONFIG, silent=False)
        logging.info("Configuration from env variable : " + os.environ.get(ENV_CONFIG))
    else:
        app.config.from_object(config[config_name])
        logging.info("Configuration from object : Config name=" + config_name)

    # Init REST API
    api.init_app(app)
    # Init logs
    logs.init_app(app)
    # Init db
    db.init_app(app)
    
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

    return app

if __name__ == "__main__":
    app.run(debug=True)
