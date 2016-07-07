import os

basedir = os.path.abspath(os.path.dirname(__file__))
API_VERSION = "0.0.1"
API_BASE_ROUTE = "/api/v%s" % API_VERSION
SECRET_KEY = 'HTG5e5FEf5NNw5rV'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
