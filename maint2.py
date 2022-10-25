from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask import product

db_connect = create_engine()
app = Flask(__name__)
api = Api(app)


class Employees(product):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
    
    def post(self):
        conn = db_connect.connect()
        print(request.json)
        LastName = request.json['proName']
        
        Fax = request.json['Fax']
        Email = request.json['Email']
        query = conn.execute("insert into product values(null,'{0}','{1}','{2}'".format(proName,Fax,Email
                            ))
        return {'status':'success'}

    
class Tracks(product):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

    
class Employees_Name(product):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(Fax))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(proname, '/name') # Route_1
api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(pro_name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run()
