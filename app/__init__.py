__doc__ = """
These are the base functions of the app.

app.py
======
contains the constructor of the app. Call create_app(config_name, config_file) to create a new app instance.

wsgi.py
=======
contains script needed for a WSGI server like uWSGI, Gunicorn...

run.py
=======
contains script that start server, for dev purpose only.

config.py
=========
contains configuration objects for development, testing and production.
These configuration probably will not be enough for you, this is why you will
need to add configuration in a config file. You pass the config file to the
create_app() call.

Directory structure
===================

models
________
contains the database models of the app

api
________
contains flasked based REST API of the app

bin
______
contains BASH scripts for starting server, clean logs, init DB...

migrations
_________
contains database management scripts, cf. Flask migrate

tools
_______
contains lib that helps coding, exemple : log management 


static
_______
contains all components that are needed for the WebUI.
"""

