# Import libraries
from flask import Flask
from flask import request, render_template
import joblib

# Instantiate flask app
app = Flask(__name__)

# Set up routes
@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        model = joblib.load("Taste")
        sugar = request.form.get('Sugar')
        milk = request.form.get('Milk')
        pred = model.predict([[float(sugar), float(milk)]])
        pred = pred[0]
        if pred == 1:
            pred = 'tasty'
        elif pred == 0:
            pred = 'not tasty'
        return render_template("index.html", result = f'Predicted chocolate taste is {pred}!')
    else:
        return render_template("index.html", result = "Please enter inputs!")

# Run app when file is ran
if __name__ == '__main__':
    app.run()
