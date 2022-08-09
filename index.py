from urllib import response
from flask import Flask
from dataConstants import studentsx
from studentsdata import students

app=Flask(__name__)

global studentsData
studentsData=students

global st_list
st_list=studentsx


@app.route('/',methods=['GET'])
def home():
    st_list.append('gama')
    return {
        'status':200,
        'response':'app working fine!',
        'data':st_list
    }

@app.route('/greet',methods=['GET'])
def Greet():
    return {"response":"hello welcome !"}

@app.route('/poem',methods=['GET'])
def poem():
    return {'poem':'nhi ati!',
    "data":st_list
    }

@app.route('/user/<string:username>',methods=['POST'])
def adduser(username):
    st_list.append(username)
    return {
        "response":"data addes succesfully!",
        "status":200
    }


@app.route('/greetbyname/<string:human>/<int:age>',methods=['GET'])
def greetings(human,age):
    return {"response":"hello {} of age {}".format(human,age)}


@app.route('/greetbyid/<int:id>',methods=['GET'])
def idnumber(id):
    return {"response":"hello {}idnumber".format(id)}

#get requests
@app.route('/getstudents',methods=['Get'])
def getstudents():
    return {
        'response':studentsData,
        'status':200
    }

@app.route('/getstudentsbyid/<int:id>',methods=['GET'])
def getstudentsbyid(id):
    return {
        "response":studentsData[id],
        "status":200
    }

@app.route('/deletebyid/<int:id>',methods=['DELETE'])
def deldata(id):
    del studentsData[id]
    return {
        "response":"students data of {} have been deleted sucessfully ".format(id),
        "status":200
    }








app.run(debug=True,port=8000)
