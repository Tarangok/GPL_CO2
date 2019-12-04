from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)


class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(ai_quotes), 200
        for quote in ai_quotes:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404

    def post(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()
      for quote in ai_quotes:
          if(id == quote["id"]):
              return f"Quote with id {id} already exists", 400
      quote = {
          "id": int(id),
          "author": params["author"],
          "quote": params["quote"]
      }
      ai_quotes.append(quote)
      return quote, 201

    def put(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("author")
      parser.add_argument("quote")
      params = parser.parse_args()
      for quote in ai_quotes:
          if(id == quote["id"]):
              quote["author"] = params["author"]
              quote["quote"] = params["quote"]
              return quote, 200
      
      quote = {
          "id": id,
          "author": params["author"],
          "quote": params["quote"]
      }
      
      ai_quotes.append(quote)
      return quote, 201

    def delete(self, id):
      global ai_quotes
      ai_quotes = [qoute for qoute in ai_quotes if qoute["id"] != id]
      return f"Quote with id {id} is deleted.", 200

class GoFuck(Resource):
    def get(self, name='0_0'):
        a = {
            'name': name,
            'text': 'Idi na XYU'
        }
        return a, 200


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
api.add_resource(GoFuck, "/", "/<string:name>")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
