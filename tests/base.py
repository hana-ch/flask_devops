import unittest

from app.app import create_app
from app.config import TestingConfig
from app.models import db
from app.models.model import Content, Other

class MyTestCase(unittest.TestCase):




    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing', "")
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.drop_all()
        db.create_all()
        db.session.add(Content("premier", "Premier contenu"))
        db.session.add(Content("2", "Et un autre"))
        db.session.add(Other("Autre 1", "une description c'est bien"))
        db.session.commit()
        
