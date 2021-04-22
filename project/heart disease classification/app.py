import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    if(prediction == '1'):
        output = 'Having Disease'
        return output
    elseif(prediction == '0'):
        output = 'Not having disease'
        return output

    return render_template('index.html', prediction_text='Your heart constition is : {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
