#! /bin/bash

FLASK_ENV=development FLASK_APP=run:app flask run -h 0.0.0.0 -p 5000
