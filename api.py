from flask import Flask, jsonify, render_template, make_response
from flask_restful import reqparse, Api, Resource
from task_03 import get_time_summary

app = Flask(__name__)
api = Api(app)

data = {"lesson": [1594692000, 1594695600],
        "pupil": [1594692033, 1594696347],
        "tutor": [1594692017, 1594692066, 1594692068, 1594696341]}

parser = reqparse.RequestParser()
parser.add_argument("lesson", action="append")
parser.add_argument("pupil", action="append")
parser.add_argument("tutor", action="append")


class Result(Resource):
    def get(self):
        return make_response(render_template("index.html", help="Usage:"), 200)

    def post(self):
        args = parser.parse_args()
        return jsonify({"Result": get_time_summary(args)})


api.add_resource(Result, "/api/1.0")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)
