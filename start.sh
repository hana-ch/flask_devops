#! /bin/bash

if [ $# = 1] 
then
	echo "Usage : ./start.sh [-c CONFIG_FILE]"
elif [ $# = 2 ] && [ $1 = "-c" ] 
then
	APP_CONFIGFILE=$2 FLASK_ENV=development FLASK_APP=run:app flask run -h 0.0.0.0 -p 5000
else 
	FLASK_ENV=development FLASK_APP=run:app flask run -h 0.0.0.0 -p 5000
fi
