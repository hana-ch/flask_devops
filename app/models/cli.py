from flask.cli import AppGroup

from . import db
from .model import Content, Other

# CLI group 
db_cli = AppGroup('data', help='Data commands')


@db_cli.command("create", help="Initialise database")
def init_data():
    # Drop database schema
    #db.drop_all()
    # Create database schema
    #db.create_all()
    # Add data in database
    db.session.add(Content("Contenu 1", "Premier contenu"))
    db.session.add(Content("2", "Et un autre"))
    db.session.add(Other("Autre 1", ""))
    db.session.commit()
    print('Base de données initialisée!')
