from app import create_app

CONFIG_NAME = "development" # production , testing

app = create_app(config_name=CONFIG_NAME)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
