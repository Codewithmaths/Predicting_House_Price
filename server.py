from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimate_price' : util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

if __name__=="__main__":
    print("Starting python flask server for home price predictino ... ")
    util.load_saved_artifacts()
    app.run()


#http://127.0.0.1:5000(get)
# http://127.0.0.1:5000/predict_home_price(post)
