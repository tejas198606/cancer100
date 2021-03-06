import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder='template')
model = pickle.load(open('model101.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('cancer.html')  

@app.route('/predict',methods=['POST'])
def predict():                              
    input_features = [float(x) for x in request.form.values()]  
    final_features = [np.array(input_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    features_name = ['age', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    
    df = pd.DataFrame(final_features, columns=features_name)
    output = model.predict(df)
    
    
    return render_template('cancer.html', prediction_text=' target {}'.format(output))



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)