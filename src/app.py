
# your code here

from flask import Flask, request, render_template
from pickle import load
import os

os.getcwd()

app = Flask(__name__)
model = load(open("/workspaces/ralexarnold-flask-machine-learning-python-template/src/best_model.pkl", "rb"))
class_dict =  { '0': 'Brown Dwarf',
                '1': 'Red Dwarf',
                '2' : 'White Dwarf',
                '3' : 'Main Sequence',
                '4' : 'Supergiant',
                '5': 'Hypergiant'}

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        
        val1 = str(request.form["val1"])
        val2 = str(request.form["val2"])
        val3 = float(request.form["val3"])
        val4 = float(request.form["val4"])
        
        data = [[val1, val2, val3, val4]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    
    return render_template("index.html", prediction = pred_class)
