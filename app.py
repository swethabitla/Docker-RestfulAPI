from flask import Flask, jsonify, render_template, request
import json


app = Flask(__name__)
jData = json.loads(open('./bestdeals.json').read())
data=jData["Clothing"]

# Intial request Ex: http://192.168.99.100:5000/
@app.route('/')
def route_main():
    return "RESTful Webservice has Started. Implement proper URL for Requesting Data"

# Returns JSON which containes all bestdeals
@app.route('/getbestdeals/')
def bestdeals_all():
    return render_template("index.html",items=data)

# Returns bestdeals JSON which matches the id
@app.route('/getbestdeals/<string:id>/')
def bestdeals_by_id(id=''):
    myList=[]
    for element in data:
        if element["id"] == id:
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the bestdeals JSON with particular categories
@app.route('/getbestdeals/categories/<string:categories>/')
def bestdeals_by_categories(categories=''):
    myList=[]
    for element in data:
        if element["categories"].lower() == categories.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the bestdeals JSON with location city
@app.route('/getbestdeals/city/<string:city>/')
def bestdeals_by_city(city=''):
    myList=[]
    for element in data:
        if element["city"].lower() == city.lower():
            myList.append(element)
    return render_template("index.html",items=myList)

# Returns the bestdeals JSON with location city and particular category 
@app.route('/getbestdeals/city/<string:city>/categories/<string:category>/')
def bestdeals_by_city_and_category(city='', category =''):
    myList=[]
    for element in data:
        if element["city"].lower() == city.lower():
             if element["categories"].lower() == category.lower():
                myList.append(element)
    #return jsonify(myList)
    return render_template("index.html",items=myList)


if __name__ == '__main__':
    app.run(host='0.0.0.0')