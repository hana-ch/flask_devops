# Fichier de configuration de l'Application Flask
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Clé obligatoire permettant de faire du chiffrement symétrique (pour les cookies Flask entre autre)
    # Génération d'une nouvelle clé, à faire obligatoirement pour chaque environnement : 
    # >>> import random, string
    # >>> "".join([random.choice(string.printable) for _ in range(24)])
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'
    # bdd sqllite3
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')



class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '#d#JCqTTW\nilK\\7m\x0bp#\tj~#H'

    # bdd mysql
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://myapp@localhost/myapp'
    # bdd postgres
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://root:password@localhost/myapp'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

