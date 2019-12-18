import logging as lg

from . import db

"""
Base class for all tables for adding and deleting records
"""
class BaseMixin(object):
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        ret = self.id
        db.session.delete(self)
        db.session.commit()
        return ret



"""
'Content' class represents 'content' table in database
"""
class Content(BaseMixin, db.Model):
    """
    Table content
    id : Primary key
    name : Name of content; not null
    description : Desc of content
    """
    __tablename__ = "content"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    #field = db.Column(db.String(200), nullable=True) # To test db upgrade; downgrade

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Content {}>".format(self.name)


class Other(BaseMixin, db.Model):
    """
    Table other
    id : Primary key
    name : Name of other; not null
    description : description 
    """
    __tablename__ = "other"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Other {}>".format(self.name)
 
