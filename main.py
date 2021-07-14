from flask import Flask, jsonify, request
from flask_restful import Api
from flask_pymongo import pymongo
import db_config as database

#Resources
from res.user import User
from res.profile import Profile
from res.goal import Goal
from res.reward import Reward
from res.career import Career
from res.transactions import Transaction


app = Flask(__name__)
api = Api(app)

@app.route('/all/school/')
def get_all_school_utch():
    response = list(database.db.Recycling.find({'school': {"$eq":"1"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)
    
@app.route('/all/school/')
def get_all_school_uach():
    response = list(database.db.Recycling.find({'school': {"$eq":"2"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/school/')
def get_all_school_itch():
    response = list(database.db.Recycling.find({'school': {"$eq":"3"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/grade/')
def get_all_grade():
    response = list(database.db.Recycling.find({'grade': {"$eq":"5"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/career/')
def get_all_career():
    response = list(database.db.Recycling.find({'carrer': {"$eq":"2"}}, {"_id":1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)


@app.route('/all/transactions/')
def get_all_user_transactions():
    response = list(database.db.Badges.find({}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/')
def get_all_user_information():
    response = list(database.db.Badges.find({}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)


api.add_resource(User, '/new/', '/<string:by>:<string:data>/')
api.add_resource(Career, '/career/<carrer>/')
api.add_resource(Profile, '/new/profile/', '/profile/<string:_id>/', '/<string:by>/<string:data>/')
api.add_resource(Transaction, '/new/transaction/<string:_id>/', '/transaction/<string:_id>/', '/<string:_id>/<string:uuid>/')
api.add_resource(Goal, '/new/goal/<string:_id>/', '/goal/<string:_id>/')
api.add_resource(Reward, '/new/reward/<string:_id>/', '/reward/<string:_id>/')


if __name__ == '__main__':
    app.run(load_dotenv = True)