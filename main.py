from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

from detoxify import Detoxify



app = Flask(__name__)
api = Api(app)

posts_get_args = reqparse.RequestParser()
posts_get_args.add_argument("text", type = str, help = "Text is required", required = True)

class Analysis(Resource):
    def get(self, postId):
        args = posts_get_args.parse_args()
        results = Detoxify('original').predict(args["text"])
        print(results)
        print(type(results))
        data = {}
        for keys in results:
            data[keys] = str(results[keys])
        
        return {postId : data}

api.add_resource(Analysis , "/post/<int:postId>")

if __name__ == "__main__":
    app.run(debug = True)
