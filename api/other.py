from flask_restplus import Namespace, Resource, fields


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
        return {'others': 'names'} 
    
    @api.doc('add_other')
    @api.marshal_with(other, code=201)
    def post(self):
        """
        Add other to other list
        """
        return {'others':'name'}, 201


@api.route('/<int:id>')
class Other(Resource):
    @api.doc('get_other')
    @api.marshal_with(other)
    def get(self, id):
        return {'other': 'name'+str(id)}

    @api.doc('update_other')
    @api.expect(other)
    @api.marshal_with(other)
    def put(self, id):
        return {'other': 'name'}

    @api.doc('delete_other')
    @api.response(204, 'Other deleted')
    def delete(self, id):
        return '', 204
