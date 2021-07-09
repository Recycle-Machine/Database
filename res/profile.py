from flask import Flask, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Profile(Resource):
    """ handeling post behavior """

    