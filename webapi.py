# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import json

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class dat(Resource):
    
    def get(self):
        with open('data.csv') as file:
            out = {'x':[], 'y':[]}
            raw = file.read().splitlines()
            for l in raw:
                crd = l.split(", ")
                out['x'].append(int(crd[0]))
                out['y'].append(int(crd[1]))
        return jsonify(out)

                
    def post(self):
        data = request.get_json()
        with open('data.csv', "a") as file:
            file.write(f"{data['x']}, {data['y']}\n")
    
    def delete(self):
        with open("data.csv", "w") as file:
            file.write("")


# adding the defined resources along with their corresponding urls 
api.add_resource(dat, '/') 


# driver function 
if __name__ == '__main__': 
	app.run(debug = True) 
