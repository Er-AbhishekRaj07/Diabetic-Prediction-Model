from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the SVM model
model = joblib.load('svm_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract user input data from the request and convert to float
    pregnancies = float(request.form.get('pregnancies', 0))
    glucose = float(request.form.get('glucose', 0))
    blood_pressure = float(request.form.get('blood_pressure', 0))
    skin_thickness = float(request.form.get('skin_thickness', 0))
    insulin = float(request.form.get('insulin', 0))
    bmi = float(request.form.get('bmi', 0))
    diabetes_pedigree_function = float(request.form.get('diabetes_pedigree_function', 0))
    age = float(request.form.get('age', 0))

    # Make the prediction using the loaded model
    input_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
    prediction = model.predict([input_data])[0]

    # Convert prediction to human-readable label
    if prediction == 0:
        result = 'Not Diabetic'
    else:
        result = 'Diabetic'

    return render_template('result.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)
