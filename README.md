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


BDD :
_____
L'application utilise le module SQLAlchemy permettant d'utiliser : sqllite, postgresql ou mysql. Cf. config.py ou config.cfg
Le template propose la gestion des mises à jour des schémas base de données automatiquement.

Strategy de migration : 
** DEV :
* Première itération :
Après récupération du template, une fois models/model.py implémenté, il faut :
- Initialiser le répertoire "migration", nécessaire pour la migration automatique de la base => cmd : flask db init
- Création du script de création des tables et création du schéma base de données, crée uniquement une table système pour la gestion de la migration => cmd : flask db migrate -m "Init"
- Créer les tables => cmd : flask db upgrade
- (facultatif) Alimenter la base de données => flask data create (commande custom qui peut être changer selon le besoin; cf. models/cli.py)

Un script existe pour faire ces opérations en un coup => ./bin/initDB.sh

* Itération++ :
Si l'on vient à changer le models/model.py ou ajouter un nouveau schéma models/model2.py par exemple :
- Création du script de mise à jour => cmd : flask db migrate [-m "commentaire"] 
Attention : 
Flask migrate ne detecte pas toutes les modifications : cf. https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect
Exemple :
Si vous changer le nom d'une table, la commande migrate ne génerera pas le bon script; il faudrat le faire à la main en modifiant migration/versions/<le_bon_fichier>.py
- Modification du schéma effective => cmd : flask db upgrade
- (facultatif) Pour revenir en arrière => cmd : flask db downgrade

Des scripts existent pour faire les opérations de migration, d'upgrade et de downgrade :
./bin/generate_scriptsDB.sh (migrate)
./bin/upgradeDB.sh 
./bin/downgradeDB.sh

En résumé :
- Après l'initDB.sh, un répertoire migration est créé à ne surtout pas supprimer. 
- Toutes modifications du schéma, impose une génération des scripts et un upgrade. 

** PROD :
* Première itération : ./initDB.sh
* Itération++ : Récupérer le nouveau package contenant le répertoire "migration", et exécuter upgradeDB.sh uniquement. 

Tests :
________
Swagger existant sur : /docs


Log :
_______
Regarder le fichier de config


WSGI : Gunicorn + NGINX
_______
Lire le tuto : https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a

CLI :
______
Les commandes CLI : 
- FLASK_APP=run.py flask db init => Initialise la bdd; crée aussi le fichier db si SQLLITE3
- FLASK_APP=run.py flask log clean => Supprime les fichiers de logs dans le répertoire de log

Des scripts existent dans ./bin pour faciliter l'exécution des commandes. 
