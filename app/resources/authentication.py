from flask_restful import Resource

class Authentication(Resource):
    def get(self, num):
        return {'status': 1, 'id':num}
    def patch(self, num):
        return {'status': 1, 'id':num}