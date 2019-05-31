from flask import Flask
from flask import jsonify
import json
import pymongo
from flask_restplus import Api, Resource

api = Api()

app = Flask(__name__)

api.init_app(app)

# da ora possiamo utilizzare le annotazioni di restplus e non più app.route
# le funzioni precedenti diventano classi

@api.route('/api/questionair/<id>')
class Questionair(Resource):
    def get(self, id):
        d = None
        try:
            with open('data.json') as f:
                d = json.load(f)
        except:
            pass

        return jsonify({"questionair":d })

# API per ricercare da un id su db

@api.route('/api/tmmQuestions/<id>')
class TmmQuestionair(Resource):
    def get(self, id):
        result = []
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient["questions"]
        mycol = mydb["questions"]

        for x in mycol.find({"course" : id}):
            del x["_id"] # poichè nel file json possiamo avere solo stringhe, numeri, None o altri json e non Object, dobbiamo eliminare Object che è la chiave creata da mongodb
            result.append(x)

        return jsonify({"DB": result})

if __name__ == '__main__':
    app.run()
