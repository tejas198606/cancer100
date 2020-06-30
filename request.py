import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':2.0000,'cp':6.0000,'trestbps':2.00000,'chol':9.00000,'fbs':6.00000,
                            'restecg':9.00000,'thalach':6.00000,'exang':20000,'oldpeak':900000,
                            'slope':60000,'ca':60000,'thal':900000})

print(r.json())