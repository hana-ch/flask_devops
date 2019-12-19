from flask_restplus import Namespace, Resource, fields
from flask import current_app

from app.models.otherDAO import OtherDAO

api = Namespace('others', description='Others related operations')

other = api.model('others', {
    'name': fields.String(required=True, description='Name of the other'),
    'description': fields.String(required=True, description='Description of the other'),
    })


@api.route('/')
class OtherList(Resource):
    @api.doc('list_other')
    @api.marshal_list_with(other)
    def get(self):
        """
        Get other list
        """
        current_app.logger.info("Applicative log example !")
        return OtherDAO().others
    
    @api.doc('add_other')
    @api.expect(other)
    @api.marshal_with(other, code=201)
    def post(self):
        """
        Add other to other list
        """
        current_app.logger.debug("Applicative debug log example !")
        return OtherDAO().create(api.payload), 201


@api.route('/<int:id>')
class Other(Resource):
    @api.doc('get_other')
    @api.marshal_with(other)
    def get(self, id):
        other = OtherDAO().get(id)
        if other:
            return other
        else:
            api.abort(404, "Other {} doesn't exist".format(id))

    @api.doc('update_other')
    @api.expect(other)
    @api.marshal_with(other)
    def put(self, id):
        return OtherDAO().update(id, api.payload)

    @api.doc('delete_other')
    @api.response(204, 'Other deleted')
    def delete(self, id):
        return OtherDAO().delete(id), 204
