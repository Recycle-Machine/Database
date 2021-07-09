from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database


class User(Resource):
    ''' Handeling the data from one badge at a time '''

    def get(self,by,data):
        response = self.abort_if_not_exist(by, data)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    

