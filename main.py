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


app = Flask(__name__)
api = Api(app)


@app.route('/all/goals/')
def get_all_user_goals():
    response = list(database.db.Badges.find({}, {'goals': 1}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

@app.route('/all/')
def get_all_user_information():
    response = list(database.db.Badges.find({}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response)

''' @app.route('/all/carrers/')
def get_all_user_by_carrer():
    response = list(database.db.Badges.find({'goals': {"$eq": 1}}, {'cardboard_quantity':'1', 'glass_quantity':'1', 'aluminium_quantity':'1'}))

    for document in response:
        document["_id"] = str(document['_id'])

    return jsonify(response) '''

@app.route('/all/carrers/')
def get_all_user_by_carrer_UTCH():
    response = list(database.db.Badges.find({'carrer': {"$eq": "0"}}, {"name": 1, "profile": 1}))

    for document in response:
        document["_id"] = str(document['_id'])


    return jsonify(response)



api.add_resource(User, '/new/', '/<string:by>:<string:data>/')
api.add_resource(Career, '/career/<carrer>/')
api.add_resource(Profile, '/new/profile/<string:_id>/', '/profile/<string:_id>/', '/<string:_id>/<string:uuid>/')
api.add_resource(Goal, '/new/goal/<string:_id>/', '/goal/<string:_id>/')
api.add_resource(Reward, '/new/reward/<string:_id>/', '/reward/<string:_id>/')


if __name__ == '__main__':
    app.run(load_dotenv = True)