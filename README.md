Template de projet Flask
=======================


Objectif:
__________
Partir d'une base commune pour les devs python.


Bien commencer :
___________
[[ Procédure à tester ]]
- cd <WORK_DIR>
- virtualenv -p <PATH_TO_PYTHON3> env 
- source env/bin/activate
- git clone https://git.digitalberry.fr/PRJ-TEMPLATE/template-flask <DIR> : cloner le projet dans <DIR>
- cd <DIR>
- git remote rename origin old-origin
- Créer un nouveau projet Git pour avoir <URL_TO_YOUR_GIT_PROJECT>
- git remote add origin <URL_TO_YOUR_GIT_PROJECT>
- git push origin <YOUR_GIT_PROJECT_BRANCH> 
- start dev...
- git add file1 file2 ...
- git commit -m "COMMENT"
- git push origin <YOUR_GIT_PROJECT_BRANCH>
- deactivate


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

__Strategy de migration :__ 
__DEV :__
_Première itération :_

Après récupération du template, une fois models/model.py implémenté, il faut :
- Supprimer le répertoire "migration"; attention à ne faire que lors de la première itération !!
- Initialiser le répertoire "migration", nécessaire pour la migration automatique de la base => cmd : flask db init
- Création du script de création des tables et création du schéma base de données, crée uniquement une table système pour la gestion de la migration => cmd : flask db migrate -m "Init"
- Créer les tables fonctionnelles et une table système pour la gestion de la migration (alembic_version) => cmd : flask db upgrade
- (facultatif) Alimenter la base de données => flask data create (commande custom qui peut être changer selon le besoin; cf. models/cli.py)

Un script existe pour faire ces opérations en un coup => ./bin/initDB.sh

_Itération++ :_
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

__PROD :__
_Première itération_
./bin/upgrade.sh
(facultatif) flask data create
_Itération++ :_ 
Récupérer le nouveau package contenant le répertoire "migration", et exécuter upgradeDB.sh uniquement. 

Tests :
________
Swagger existant sur : /docs


Tests unitaires :
_________________
Les tests unitaires sont décrits dans le répertoire "tests".
Pour les éxécuter tous : 
python -m unittest discover /path/to/tests


Log :
_______
Regarder le fichier de config


WSGI : Gunicorn + NGINX
_______
Lire le tuto : https://medium.com/faun/deploy-flask-app-with-nginx-using-gunicorn-7fda4f50066a

CLI :
______
Pour avoir un aperç des commandes possibles, exécuter : FLASK_APP=run.py flask
Il y a des commandes générées par Flask ou ses extensions et d'autres commandes custom (ex: tools/cli.py ou models/cli.py)
Les commandes CLI : 
- FLASK_APP=run.py flask data create => Alimente la bdd avec des données
- FLASK_APP=run.py flask log clean => Supprime les fichiers de logs dans le répertoire de log

Des scripts existent dans ./bin pour faciliter l'exécution des commandes. 
