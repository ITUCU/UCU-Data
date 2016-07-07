from app import app, utils
from flask_restful import Api, Resource
from app.resources.authentication import Authentication
api = Api(app)

api.add_resource(Authentication, '%s/login/<regex("\d+"):num>'% app.config['API_BASE_ROUTE'])

if __name__ == '__main__':
    app.run(debug = True)
