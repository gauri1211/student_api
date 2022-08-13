@app.route('/changedata/<int:id>/',methods=['PUT'])
# def changedata_(id): 
#     changeddata=request.get_json()
#     for key in changeddata:
#         studentsData[id][key]=changeddata[key]
#     return{
#         "response":"data modified successfully!",
#         "status":200,
#         "data":studentsData[id]
#     }    