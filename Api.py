# API : Application programming interface
# API is used to send/recieve data on a server using external script. 
# Response status codes:
#   1xx : Informational.
#   2xx : Sucess
#   3xx : Redirection.
#   4xx : Client error.
#   5xx : Server error.
# JSON is standard for data transformation in APIs
# hame ksi application ko ksi database sy values pass karni hoti hen, magar ham us application ko database ka direct access nahi dena chahye to ham API use karty hen, application API ko call karti h, or API database par query run kar k application ko result send kar deti h.
# CRUD:
#   crete : POST
#   read  : GET
#   update: PUT
#   delete: DELETE
# An API is allows us to send a range of GET/POST/PUT/PATCH/DELETE requests (more on this later), to different endpoints, and return or modify data connected to our API.



from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast



############################################ DB
# from flask import Flask, jsonify, render_template, request
# from flask_mysqldb import MySQL
# import MySQLdb

# app = Flask(__name__)
# app.secret_key = "" # set the secret key for the production
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'pass'
# app.config['MYSQL_DB'] = 'login'

# db = MySQLdb(app)

# courses = [
#     {'courseID' : 1, 'courseName': 'Course_1'},
#     {'courseID' : 2, 'courseName': 'Course_2'},
#     {'courseID' : 3, 'courseName': 'Course_3'},
#     {'courseID' : 4, 'courseName': 'Course_4'}
# ]

# @app.route("/")
# def index():
#     return render_template("index.html")
 

# @app.route("/app/api/courses/all")
# def show():
#     cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute("SELECT * from courses")
#     info = cursor.fetchall()
#     return jsonify(info)

#     # return jsonify(courses)

# @app.route("/app/api/courses", methods=["GET"])
# def id():
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "unknow request"

#     result = []

#     for course in courses:
#         if course['courseID'] == id:
#             result.append(course)
#     return jsonify(result)



# if __name__ == "__main__":
#     app.run(debug=True)


# # TEST
# # import requests
# # base = "http://127.0.0.1:5000/app/api/courses"
# # p = ["/all", "?id=1"]
# # for pp in p:
# #   response = requests.get(pp)
# #   print(response.status_code)
# #   print(response.json())
# #   print("----------------------------\n")
################################################


app = Flask(__name__)
api = Api(app)

# To create an endpoint, we define a Python class (with any name you want) and connect it to our desired endpoint with api.add_resource
# Flask needs to know that this class is an endpoint for our API, and so we pass <Resource> in with the class definition.
class Users(Resource):
    # here we include our HTTP methods (GET, POST, DELETE, etc.). 
    def get(self):
        data = pd.read_csv('users.csv')  # read local CSV
        data = data.to_dict()  # convert dataframe to dict
        return {'data': data}, 200  # return data and 200 OK

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('users.csv')

        if args['userId'] in list(data['userId']):
            return {
                'message': f"'{args['userId']}' already exists."
            }, 409
        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'userId': [args['userId']],
                'name': [args['name']],
                'city': [args['city']],
                'locations': [[]]
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            data.to_csv('users.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('userId', required=True)  # add args
        parser.add_argument('location', required=True)
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('users.csv')
        
        if args['userId'] in list(data['userId']):
            # evaluate strings of lists to lists !!! never put something like this in prod
            data['locations'] = data['locations'].apply(
                lambda x: ast.literal_eval(x)
            )
            # select our user
            user_data = data[data['userId'] == args['userId']]

            # update user's locations
            user_data['locations'] = user_data['locations'].values[0] \
                .append(args['location'])
            
            # save back to CSV
            data.to_csv('users.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200

        else:
            # otherwise the userId does not exist
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404

    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('userId', required=True)  # add userId arg
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('users.csv')
        
        if args['userId'] in list(data['userId']):
            # remove data entry matching given userId
            data = data[data['userId'] != args['userId']]
            
            # save back to CSV
            data.to_csv('users.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        else:
            # otherwise we return 404 because userId does not exist
            return {
                'message': f"'{args['userId']}' user not found."
            }, 404

                    
# To create an endpoint, we define a Python class (with any name you want) and connect it to our desired endpoint with api.add_resource
# Flask needs to know that this class is an endpoint for our API, and so we pass <Resource> in with the class definition.
class Locations(Resource):
    # here we include our HTTP methods (GET, POST, DELETE, etc.). 
    def get(self):
        data = pd.read_csv('locations.csv')  # read local CSV
        return {'data': data.to_dict()}, 200  # return data dict and 200 OK
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('locationId', required=True, type=int)  # add args
        parser.add_argument('name', required=True)
        parser.add_argument('rating', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('locations.csv')
    
        # check if location already exists
        if args['locationId'] in list(data['locationId']):
            # if locationId already exists, return 401 unauthorized
            return {
                'message': f"'{args['locationId']}' already exists."
            }, 409
        else:
            # otherwise, we can add the new location record
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'locationId': [args['locationId']],
                'name': [args['name']],
                'rating': [args['rating']]
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            data.to_csv('locations.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK
    
    def patch(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('locationId', required=True, type=int)  # add args
        parser.add_argument('name', store_missing=False)  # name/rating are optional
        parser.add_argument('rating', store_missing=False)
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('locations.csv')
        
        # check that the location exists
        if args['locationId'] in list(data['locationId']):
            # if it exists, we can update it, first we get user row
            user_data = data[data['locationId'] == args['locationId']]
            
            # if name has been provided, we update name
            if 'name' in args:
                user_data['name'] = args['name']
            # if rating has been provided, we update rating
            if 'rating' in args:
                user_data['rating'] = args['rating']
            
            # update data
            data[data['locationId'] == args['locationId']] = user_data
            # now save updated data
            data.to_csv('locations.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        
        else:
            # otherwise we return 404 not found
            return {
                'message': f"'{args['locationId']}' location does not exist."
            }, 404
    
    def delete(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('locationId', required=True, type=int)  # add locationId arg
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('locations.csv')
        
        # check that the locationId exists
        if args['locationId'] in list(data['locationId']):
            # if it exists, we delete it
            data = data[data['locationId'] != args['locationId']]
            # save the data
            data.to_csv('locations.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        
        else:
            # otherwise we return 404 not found
            return {
                'message': f"'{args['locationId']}' location does not exist."
            }


api.add_resource(Users, '/users')           # '/users'     is our entry point for Users
api.add_resource(Locations, '/locations')   # '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()  # run our Flask app