from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#need to use this to get from database in future via CSV file
tabPrdn=[
    {"Batch_No": 1, "API_Particle_Size": "Large", "Screen_Size":4, "Blend_Time": 13.7, "Compressor": "Compressor1", "Inlet_Temp": 106.3, "Spray_Rate": 394.4, "Dissolution":71.35},
    {"Batch_No": 2, "API_Particle_Size": "Large", "Screen_Size":3, "Blend_Time": 14.1, "Compressor": "Compressor1", "Inlet_Temp": 108.8, "Spray_Rate": 388.6, "Dissolution":71.95}, 
    {"Batch_No": 3, "API_Particle_Size": "Large", "Screen_Size":4, "Blend_Time": 13.8, "Compressor": "Compressor1", "Inlet_Temp": 107.9, "Spray_Rate": 401, "Dissolution":70.34}, 
    {"Batch_No": 4, "API_Particle_Size": "Large", "Screen_Size":3, "Blend_Time": 11.9, "Compressor": "Compressor1", "Inlet_Temp": 105.7, "Spray_Rate": 395, "Dissolution":75.08},
    {"Batch_No": 5, "API_Particle_Size": "Large", "Screen_Size":4, "Blend_Time": 14.9, "Compressor": "Compressor1", "Inlet_Temp": 106.6, "Spray_Rate": 403.1, "Dissolution":73.2} 
]

nextBatch=6

@app.route('/')
def index():
    return "hello"

#get all
# curl http://127.0.0.1:5000/tabPrdn
@app.route('/tabPrdn')
def getAll():
    return jsonify(tabPrdn)

# find by Batch_No
@app.route('/tabPrdn/<int:Batch_No>')
def findByBatchID(Batch_No):
    foundBatch = list(filter (lambda t : t["Batch_No"]== Batch_No, tabPrdn))
    if len(foundBatch) == 0:
        return jsonify({}), 204
    #print (foundBatch)
    return jsonify(foundBatch[0])

#Create (#want to give options for some attributes)
#curl -X POST -H "content-type:application/json" -d "{\"API_Particle_Size\":\"MIDDLE\", \"Screen_Size\":5, \"Blend_Time\": 15, \"Compressor\": \"Compressor2\", \"Inlet_Temp\": 110, \"Spray_Rate\": 400, \"Dissolution\":75}" http://127.0.0.1:5000/tabPrdn
@app.route('/tabPrdn', methods=['POST'])
def create():
    global nextBatch
    if not request.json:
        abort(400)

    tabPrd = {
        "Batch_No": nextBatch, 
        "API_Particle_Size": request.json["API_Particle_Size"], #want to give options - large, middle, small
        "Screen_Size": request.json["Screen_Size"], #want to give options - 3, 4, 5
        "Blend_Time": request.json["Blend_Time"], 
        "Compressor": request.json["Compressor"], #want to give options - compressor1 or compressor2
        "Inlet_Temp": request.json["Inlet_Temp"], 
        "Spray_Rate": request.json["Spray_Rate"], 
        "Dissolution": request.json["Dissolution"] 
    }
    tabPrdn.append(tabPrd)
    nextBatch += 1
    return jsonify(tabPrd)
    

#update
#λ curl -X PUT -d "{\"API_Particle_Size\":\"SMALL\", \"Screen_Size\":5, \"Blend_Time\": 15, \"Compressor\": \"Compressor2\", \"Inlet_Temp\": 110, \"Spray_Rate\": 400, \"Dissolution\":750}" -H "content-type:application/json" http://127.0.0.1:5000/tabPrdn/2
@app.route('/tabPrdn/<int:Batch_No>', methods=['PUT'])
def update(Batch_No):
    foundBatch = list(filter (lambda t : t["Batch_No"]== Batch_No, tabPrdn))
    if len(foundBatch) == 0:
        return jsonify({}), 404
    currentBatch = foundBatch[0]
    if 'Batch_No' in request.json:
        currentBatch['Batch_No'] = request.json['Batch_No']
    if 'API_Particle_Size' in request.json:
        currentBatch['API_Particle_Size'] = request.json['API_Particle_Size']    
    if 'Screen_Size' in request.json:
        currentBatch['Screen_Size'] = request.json['Screen_Size']        
    if 'Blend_Time' in request.json:
        currentBatch['Blend_Time'] = request.json['Blend_Time']  
    if 'Compressor' in request.json:
        currentBatch['Compressor'] = request.json['Compressor'] 
    if 'Inlet_Temp' in request.json:
        currentBatch['Inlet_Temp'] = request.json['Inlet_Temp'] 
    if 'Spray_Rate' in request.json:
        currentBatch['Spray_Rate'] = request.json['Spray_Rate'] 
    if 'Dissolution' in request.json:
        currentBatch['Dissolution'] = request.json['Dissolution'] 

    return jsonify(currentBatch)

#delete
# curl -X DELETE http://127.0.0.1:5000/tabPrdn/5
@app.route('/tabPrdn/<int:Batch_No>', methods=['DELETE'])
def delete(Batch_No):
    foundBatch = list(filter (lambda t : t["Batch_No"]== Batch_No, tabPrdn))
    if len(foundBatch) == 0:
        return jsonify({}), 404
    tabPrdn.remove(foundBatch[0])  

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)