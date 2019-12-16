from flask_restplus import Namespace, Resource, fields
from flask import current_app


api = Namespace('contents', description='Contents related operations')

content = api.model('Content', {
    'name' : fields.String(required=True, description='Name of the content'),
    'description' : fields.String(required=True, description='Description of the content'),
    })


@api.route('/')
class ContentList(Resource):

    @api.doc('list_content')
    @api.marshal_list_with(content)
    def get(self):
        """
        Get content list
        """
        current_app.logger.info("Applicative log example !")

        return {'contents': 'names'} 
    
    @api.doc('add_content')
    @api.marshal_with(content, code=201)
    def post(self):
        """
        Add content to content list
        """
        current_app.logger.debug("Applicative debug log example !")
        return {'contents':'name'}, 201


@api.route('/<int:id>')
class Content(Resource):
    @api.doc('get_content')
    @api.marshal_with(content)
    def get(self, id):
        return {'content': 'name'+str(id)}

    @api.doc('update_content')
    @api.expect(content)
    @api.marshal_with(content)
    def put(self, id):
        return {'content': 'name'}

    @api.doc('delete_content')
    @api.response(204, 'Content deleted')
    def delete(self, id):
        return '', 204
