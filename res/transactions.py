from flask import Flask, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Transaction(Resource):
    """ handeling transaction behavior """

    def get(self, _id):
        response = self.abort_if_not_exist(_id)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self, _id):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({"_id": ObjectId(_id)}, {"$push":{
            "transaction":{
                "id": request.json["id"],
                "glass": request.json["glass"],
                "plastic": request.json["plastic"],
                "aluminum": request.json["aluminum"],
            }
        }})

        return jsonify({"message": f"The transaction {request.json['id']} was successfully created"})

    def put(self, _id, uuid):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({"_id": ObjectId(_id), "transaction.id": uuid},
        {"$set":{
            "profile.$.glass": request.json["glass"],
            "profile.$.plastic": request.json["plastic"],
            "profile.$.aluminum": request.json["aluminum"],

        }})

        return jsonify(request.json)
        
    def abort_if_not_exist(self, _id):
        response = database.db.Badges.find_one({'_id':ObjectId(_id)}, {"name": 1, "transaction": 1})

        if response:
            return response
        else:
            abort(jsonify({"status": 404, "_id": f"{_id} not found"}))