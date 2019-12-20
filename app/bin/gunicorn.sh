#! /bin/bash 

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH/../..

arg_number=$# 

if [ $arg_number -eq 1 ]; then 	
	echo "Usage : ./start.sh [-c CONFIG_FILE]" 
elif [ $arg_number -eq 2 ] && [ $1 = "-c" ]; then 	
	APP_CONFIGFILE=$2 FLASK_ENV=production gunicorn --bind 0.0.0.0:5000 app.wsgi:app 
else 	
	APP_CONFIGFILE='./config.cfg' FLASK_ENV=production gunicorn --bind 0.0.0.0:5000 app.wsgi:app
fi


