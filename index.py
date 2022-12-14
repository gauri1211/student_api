from inspect import isdatadescriptor
from urllib import response
from flask import Flask,request
from dataConstants import studentsx
from studentsdata import students

app=Flask(__name__)

global studentsData
studentsData=students

global stid
stid=8

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

@app.route('/addstudent/',methods=['POST'])
def addstudnts():
   
    ext_data=request.get_json()
    print(ext_data)
  
    studentsData[9]=ext_data

    return {
        "response":"data addd successfully!",
        "status":200
    } 

@app.route('/modifydata/<int:id>/',methods=['PUT'])
def modifystudent(id):
    stored_data=request.get_json()
    studentsData[id]=stored_data
    return{
        "response":"data modified successfully!",
        "status":200
    }

@app.route('/changedata/<int:id_>/',methods=['PUT'])
def changedata_(id_): 
    changeddata=request.get_json()
    for key in changeddata:
        studentsData[id_][key]=changeddata[key]
    return{
        "response":"data modified successfully!",
        "status":200,
        "data":studentsData[id_]
    }    

        

@app.route('/deletebyid/<int:id>',methods=['DELETE'])
def deldata(id):
    del studentsData[id]
    return {
        "response":"students data of {} have been deleted sucessfully ".format(id),
        "status":200
    }








app.run(debug=True,host="0.0.0.0")
