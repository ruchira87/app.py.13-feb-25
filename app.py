from flask import Flask, jsonify, request, make_response


app = Flask(__name__)

businesses = [
{
    "id":1,
    "Name":"Ruchira Tex",
    "Location":"Gravesend",
    "Ratings":"5",
    "Reviews":[]
},
{
    "id":2,
    "Name":"Ruwani tex",
    "Location":"Farringdon",
    "Ratings":"5",
    "Reviews":[]
},
{
    "id":3,
    "Name":"Ravindu tex",
    "Location":"London",
    "Ratings":"5",
    "Reviews":[]
}]

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to COM661"})

@app.route('/businesses', methods=['GET'])
def get_all_businesses():
    return make_response (jsonify({"businesses":businesses }),200)

@app.route("/businesses",methods=['POST'])
def add_business():
    data = request.form
    id = businesses[-1]["id"]+1
    new_business = {
        "id":id,
        "Name":data.get("Name"),
        "Location":data.get("Location"),
        "Ratings":data.get("Ratings",0),
        "Reviews":[]
    }
    businesses.append(new_business)
    return make_response(jsonify(new_business),201) 

@app.route("/businesses/<int:biz_id>",methods=['GET'])
def get_one_id_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id:
            return make_response(jsonify(biz),200)
    else:
        return make_response(jsonify({"error":"not found"}),400)

@app.route("/businesses/<int:biz_id>",methods=['PUT'])
def edit_business(biz_id):
    data = request.form
    for biz in businesses:
           if biz["id"] == biz_id:        
                biz["Name"]=data.get("Name"),
                biz["Location"]=data.get("Location"),
                biz["Ratings"]=data.get("Ratings"),
                biz["Reviews"]=[]
                break
    return make_response(jsonify(biz),200) 

@app.route("/businesses/<int:biz_id>",methods=['DELETE'])
def delete_business(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id: 
             businesses.remove(biz)
        break
    return make_response(jsonify(biz),200) 
         
@app.route("/businesses/<int:biz_id>/Reviews",methods=['GET'])
def get_all_reviews(biz_id):
    for biz in businesses:
        if biz["id"] == biz_id: 
            break
    return make_response(jsonify(biz["Reviews"]),200) 

@app.route("/businesses/<int:biz_id>/Reviews",methods=['POST'])
def add_new_review(biz_id):
    data = request.form
    for biz in businesses:
        if biz["id"]==biz_id:
            if len(biz["Reviews"])==0:
                new_reveiw_id= 1
            else:
                new_reveiw_id = biz["Reviews"][-1]["id"]+1
            new_reveiw = {
                "id":new_reveiw_id,
                "username":data.get("username"),
                "comment":data.get("comment"),
                "star":data.get("star")            
            }
            biz["Reviews"].append(new_reveiw)
            break
    return make_response(jsonify(new_reveiw),200) 

if __name__ == '__main__':
    app.run(debug=True)

#python app.py