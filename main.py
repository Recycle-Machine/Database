from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
import db_config as database

#Resources
from badge import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/new/', '/<string:by>:<string:data>/')

if __name__ == '__main__':
    app.run(load_dotenv = True)