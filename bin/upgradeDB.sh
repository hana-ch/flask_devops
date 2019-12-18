#! /bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH/..

# Apply script
FLASK_APP=run.py flask db upgrade
