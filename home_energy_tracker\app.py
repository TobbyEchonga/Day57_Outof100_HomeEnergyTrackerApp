from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Sample data structure (replace this with your actual data)
energy_data = pd.DataFrame({
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
    'Electricity': [150, 180, 200],
    'Gas': [20, 25, 30]
})

@app.route('/')
def index():
    return render_template('index.html', energy_data=energy_data.to_dict(orient='records'))

@app.route('/add', methods=['POST'])
def add_reading():
    date = request.form['date']
    electricity = float(request.form['electricity'])
    gas = float(request.form['gas'])

    new_reading = pd.DataFrame({
        'Date': [date],
        'Electricity': [electricity],
        'Gas': [gas]
    })

    global energy_data
    energy_data = pd.concat([energy_data, new_reading], ignore_index=True)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
