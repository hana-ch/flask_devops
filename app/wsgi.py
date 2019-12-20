from .app import create_app

app = create_app(config_name="production", config_file="/etc/flask_app/config.cfg")
