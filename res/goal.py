from flask import Flask, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Goal(Resource):
    """ handeling goal behavior """

    def get(self, _id):
        response = self.abort_if_not_exist(_id)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self, _id):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({"_id": ObjectId(_id)}, {"$push":{
            "goal":{
                "id": request.json["id"],
                "type": request.json["type"],
                "cardboard_quantity": request.json["cardboard_quantity"],
                "glass_quantity": request.json["glass_quantity"],
                "aluminium_quantity": request.json["aluminium_quantity"],
            }
        }})

        return jsonify({"message": f"The goal {request.json['id']} was successfully created"})


    def abort_if_not_exist(self, _id):
        response = database.db.Badges.find_one({'_id':ObjectId(_id)}, {"name": 1, "goal": 1})

        if response:
            return response
        else:
            abort(jsonify({"status": 404, "_id": f"{_id} not found"}))