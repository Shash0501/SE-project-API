from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from numpy import random
from detoxify import Detoxify



app = Flask(__name__)
api = Api(app)

posts_get_args = reqparse.RequestParser()
posts_get_args.add_argument("text", type = str)

test_get_args = reqparse.RequestParser()
test_get_args.add_argument("text", type = str)

class Analysis(Resource):
    def get(self, postId):
        print(postId)
        request.args.get("text")
        text = request.args['text']
        print(text)
        results = Detoxify('original').predict(text)
        print(results)
        print(type(results))
        data = {}
        for keys in results:
            data[keys] = str(results[keys])
        return data

api.add_resource(Analysis , "/post/<int:postId>")

class Test(Resource):
    def get(self):
        args = test_get_args.parse_args()
        print(args["text"])
        return {"data" : args["text"]}

api.add_resource(Test , "/test")

if __name__ == "__main__":
    app.run(debug =  False , host="0.0.0.0")
