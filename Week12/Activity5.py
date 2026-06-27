from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculate():
    kilograms = 0
    meters = 0
    if request.method == 'POST':
        try:
            kilograms = float(request.form.get('kilograms'))
            meters = float(request.form.get('meters'))

            if meters != 0:
                bmi_result = kilograms / meters ** 2
            else:
                bmi_result = 'Meters should not be set to zero'
        except:
            bmi_result = 'Please enter valid values'
    else:
        bmi_result = 'Please enter values to calculate'

    return render_template('activity.html', bmi_result=bmi_result, kilograms=kilograms, meters=meters)

if __name__ == '__main__':
    app.run(debug=True)
