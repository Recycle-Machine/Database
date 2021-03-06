from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class User(Resource):
    ''' Handeling the data from one user at a time '''

    def get(self,by,data):
        response = self.abort_if_not_exist(by, data)
        response['_id'] = str(response['_id'])
        
        return jsonify(response)

    def post(self):
        _id = str(database.db.user.insert_one({
            'name': request.json['name'],
            'city': request.json['city'],
            'age': request.json['age'],
            'school': request.json['school'],
            'career': request.json['career'],
        }).inserted_id)

        return jsonify({"_id": _id})

    def put(self, by, data):
        response = self.abort_if_not_exist(by, data)

        for key, value in request.json.items():
            response[key] = value

        database.db.user.update_one({'_id':ObjectId(response['_id'])},
        {'$set':{
            'name': request.json['name'],
            'city': request.json['city'],
            'age': request.json['age'],
            'school': request.json['school'],
            'career': request.json['career'],
        }})

        response['_id'] = str(response['_id'])
        return jsonify(response)

    def abort_if_not_exist(self,by,data):
        if by == "_id":
            response = database.db.user.find_one({"_id":ObjectId(data)})
        else:
            response = database.db.user.find_one({f"{by}": data})

        if response:
            return response
        else:
            abort(jsonify({"status":404, f"{by}": f"{data} not found"}))