import joblib
from flask import Flask, render_template, request
from helpers.dummies import *
import xgboost


app = Flask(__name__)

scaler = joblib.load('models/scaler.h5')
columns = joblib.load('models/columns.h5')
model = xgboost.XGBClassifier()
model.load_model('models/model.model')


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/predict', methods=['GET'])
def predict():
    all_data=request.args
    age = int(all_data['age'])
    gender = int(all_data['gender'])
    education = education_level[all_data['education']]
    marital = marital_status[all_data['marital']]
    dependent_count = int(all_data['Dependent_count'])
    income = income_type[all_data['income']]
    card = card_type[all_data['card_type']]
    months_on_book = int(all_data['Months_on_book'])
    total_relationship_count = int(all_data['Total_Relationship_Count'])
    months_inactive = int(all_data['Months_Inactive_12_mon'])
    contacts_count = int(all_data['Contacts_Count_12_mon'])
    credit_limit = float(all_data['Credit_Limit'])
    total_revolving_bal = float(all_data['Total_Revolving_Bal'])
    avg_open_to_buy = float(all_data['Avg_Open_To_Buy'])
    total_amt_chng_q4_q1 = float(all_data['Total_Amt_Chng_Q4_Q1'])
    total_trans_amount = float(all_data['Total_Trans_Amt'])
    total_trans_count = int(all_data['Total_Trans_Ct'])
    total_ct_chng_q4_q1 = float(all_data['Total_Ct_Chng_Q4_Q1'])
    avg_utilization_ratio = float(all_data['Avg_Utilization_Ratio'])

    data = [age, dependent_count, months_on_book, total_relationship_count, 
    months_inactive, contacts_count, credit_limit, total_revolving_bal, 
    avg_open_to_buy, total_amt_chng_q4_q1, total_trans_amount, total_trans_count, 
    total_ct_chng_q4_q1, avg_utilization_ratio, gender]

    all_data = data + education + marital + income + card

    data_scaled = scaler.transform([all_data])

    pred = model.predict(data_scaled)[0]

    if pred == 0:
        out = 'Not Leave'
    else:
        out = 'Leave'
    return render_template('index.html', prediction=out)



if __name__ == "__main__":
    app.run(debug=True)