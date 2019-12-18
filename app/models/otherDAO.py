from .model import Other
from . import db

class OtherDAO(object):

    @property
    def others(self):
        return Other.query.all()

    def get(self, id):
        other = Other.query.filter_by(id=id).first()
        if other:
            return {"id":other.id, "name":other.name, "description":other.description}
        return None

    def create(self, data):
        other = Other(data["name"], data["description"])
        other.save()
        return other

    def update(self, id, data):
        Other.query.filter_by(id=id).update({"name":data["name"], "description":data["description"]})
        db.session.commit()
        return {"id":id, "name":data["name"], "description":data["description"]}

    def delete(self, id):
        Other.query.filter_by(id=id).first().delete()





