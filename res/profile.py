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

    

    def abort_if_not_exist(self, _id):
        response = database.db.Badges.find_one({'_id':ObjectId(_id)}, {"name": 1, "profile": 1})

        if response:
            return response
        else:
            abort(jsonify({"status": 404, "_id": f"{_id} not found"}))