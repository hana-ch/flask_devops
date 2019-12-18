from flask_restplus import Api

from .content import api as content_api
from .other import api as other_api

api = Api(
    title='API Title',
    version='1.0',
    description='A simple demo API',
    doc = '/docs'
)

api.add_namespace(content_api)
api.add_namespace(other_api)
