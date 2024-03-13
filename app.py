from flask import Flask,request,render_template,jsonify

import json
app=Flask(__name__)
@app.route('/')
def welcome():
    return "welcome to flask"

@app.route('/cal',methods=["GET"])
def math_op():
    op=request.json["op"]
    num1=request.json["num1"]
    num2=request.json["num2"]
    if op=="add":
        res=int(num1)+int(num2)
    elif op=="sub":
        res=int(num1)-int(num2)
    elif op=="multiply":
        res=int(num1)*int(num2)
    else:
        res=int(num1)/int(num2)
    return jsonify(res)


  

if __name__=="__main__":
    app.run(debug=True)