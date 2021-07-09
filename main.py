from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
import db_config as database

#Resources
from res.user import User
from res.profile import Profile
from res.transactions import Transactions

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/new/', '/<string:by>:<string:data>/')
api.add_resource(Transactions, '/new/transactions/<string:_id>/', '/transactions/<string:_id>/')
api.add_resource(Profile, '/new/profile/<string:_id>/', '/profile/<string:_id>/', '/<string:_id>/<string:uuid>/')


if __name__ == '__main__':
    app.run(load_dotenv = True)