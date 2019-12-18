#! /bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH/..

# Init
FLASK_APP=run.py flask db init
# Create script
FLASK_APP=run.py flask db migrate -m "Init"
# Apply script
FLASK_APP=run.py flask db upgrade
# Create data in database
FLASK_APP=run.py flask data create
