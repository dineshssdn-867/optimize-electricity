from flask import Flask, request, jsonify, render_template
from sklearn.neighbors import KNeighborsClassifier
import pickle
from initalize_one_model import neigh


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('service.html')

@app.route('/check_for_faults')
def check_for_faults():
    return render_template('fault_detection.html')


@app.route('/calculate_power', methods=['POST'])
def calculate_power():
    if request.method == 'POST':
        try:
            # Get input parameters from the request
            phase_a_current = float(request.form['Phase_A_line_current'])
            phase_b_current = float(request.form['Phase_B_line_current'])
            phase_c_current = float(request.form['Phase_C_line_current'])
            phase_a_voltage = float(request.form['Phase_A_line_voltage'])
            phase_b_voltage = float(request.form['Phase_B_line_voltage'])
            phase_c_voltage = float(request.form['Phase_C_line_voltage'])

            # Perform some basic calculations (e.g., power calculation)
            result = neigh.predict([[phase_a_current,phase_b_current,phase_c_current,phase_a_voltage,phase_b_voltage,phase_c_voltage]])
            result = "Not Faulty" if result[0] == 0 else "Faulty"
            return render_template('fault_detection.html',fault=result)
        except Exception as e:
            print(e)
            return render('fault_detection.html')


if __name__ == '__main__':
    app.run(debug=True)
