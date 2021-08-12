from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
import db_config as database


class Scores(Resource):
    """ Get all users """
    def get(self):
        response = list(database.db.user.find())

        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)