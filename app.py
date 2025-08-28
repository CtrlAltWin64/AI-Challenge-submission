from flask import Flask, render_template, request
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load your trained ML model (make sure model.pkl exists in your project folder)
model = joblib.load("battery_optimizer_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input values from form
        battery = float(request.form['battery'])
        brightness = float(request.form['brightness'])
        apps = float(request.form['apps'])
        usage = float(request.form['usage'])

        # Prepare features for ML model
        features = np.array([[battery, brightness, apps, usage]])

        # Make prediction
        prediction = model.predict(features)

        # Send prediction back to HTML page
        return render_template('index.html', prediction_text=f"🔋 Predicted Result: {prediction[0]}")
    
    except Exception as e:
        # Handle errors gracefully
        return render_template('index.html', prediction_text=f"⚠ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)