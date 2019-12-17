from .model import Content
from . import db

class ContentDAO(object):

    @property
    def contents(self):
        return Content.query.all()

    def get(self, id):
        content = Content.query.filter_by(id=id).first()
        if content:
            return {"id":content.id, "name":content.name, "description":content.description}
        return None

    def create(self, data):
        content = Content(data["name"], data["description"])
        content.save()
        return content

    def update(self, id, data):
        Content.query.filter_by(id=id).update({"name":data["name"], "description":data["description"]})
        db.session.commit()
        return {"id":id, "name":data["name"], "description":data["description"]}

    def delete(self, id):
        Content.query.filter_by(id=id).first().delete()





