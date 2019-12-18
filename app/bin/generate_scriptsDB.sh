#! /bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH/..

arg_number=$#
if [ $arg_number -eq 1 ]; then
	echo "Usage : ./start.sh [-m COMMENTAIRE]"
elif [ $arg_number -eq 2 ] && [ $1 = "-m" ] 
then
	FLASK_APP=run.py flask db migrate -m "$2"
else 
	FLASK_APP=run.py flask db migrate 
fi
