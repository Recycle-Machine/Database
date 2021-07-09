from flask import Flask, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Profile(Resource):
    """ handeling post behavior """

    def get(self, _id):
        response = self.abort_if_not_exist(_id)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self, _id):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({"_id": ObjectId(_id)}, {"$push":{
            "profile":{
                "id": request.json["id"],
                "name": request.json["name"],
                "last name": request.json["last_name"],
                "state": request.json["state"],
                "city": request.json["city"],
                "enrollment": request.json["enrollment"],
                "zip code": request.json["zip_code"],
            }
        }})

        return jsonify({"message": f"The post {request.json['id']} was successfully created"})

    def put(self, _id, uuid):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({"_id": ObjectId(_id), "profile.id": uuid},
        {"$set":{
            "profile.$.name": request.json["name"],
            "profile.$.last name": request.json["last_name"],
            "profile.$.state": request.json["state"],
            "profile.$.city": request.json["city"],
            "profile.$.enrollment": request.json["enrollment"],
            "profile.$.zip code": request.json["zip_code"],
        }})

        return jsonify(request.json)

    def abort_if_not_exist(self, _id):
        response = database.db.Badges.find_one({'_id':ObjectId(_id)}, {"name": 1, "profile": 1})

        if response:
            return response
        else:
            abort(jsonify({"status": 404, "_id": f"{_id} not found"}))