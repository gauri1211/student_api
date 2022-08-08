from flask import Flask
from dataConstants import students

app=Flask(__name__)

global st_list
st_list=students


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


app.run(debug=True,port=8000)
