Template de projet Flask
=======================


Objectif:
__________
Partir d'une base commune pour les devs python.


Bien commencer :
___________
Cloner le repo, démarrer un env virtuel python et changer ensuite le repo de destination
Procedure à completer...


Démarrage :
___________
./start.sh
ou
./start.sh -c "fichier de config"
ou
export APP_CONFIGFILE="/path/to/file.cfg"; ./start.sh

Exemple :
./start.sh -c config.cfg


Tests :
________
Swagger existant sur : /docs


Log :
_______
Regarder le fichier de config


WSGI : Gunicorn + NGINX
_______
Lire le tuto : https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a

