from flask import Flask , request , jsonify , render_template
import pandas as pd
from utils import Life_Expectancy


app=Flask(__name__)


dataset=pd.read_csv(r'data/Life_Data.csv')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/Country')
def get_Country_options():
    Country_options = dataset['Country'].unique().tolist()
    return jsonify(Country_options)

@app.route('/api/Status')
def get_Status_options():
    Status_options = dataset['Status'].unique().tolist()
    return jsonify(Status_options)


@app.route('/api/predict',methods=['POST'])
def predict():
  
    Country = request.form.get('Country')
    Year=request.form.get('Year')
    Status = request.form.get('Status')
    Adult_Mortality=request.form.get('Adult_Mortality')
    infant_deaths=request.form.get('infant_deaths')
    Alcohol=request.form.get('Alcohol')
    percentage_expenditure=request.form.get('percentage_expenditure')
    Hepatitis_B=request.form.get('Hepatitis_B')
    Measles=request.form.get('Measles')
    BMI=request.form.get('BMI')
    under_five_deaths=request.form.get('under-five_deaths')
    Polio=request.form.get('Polio')
    Total_expenditure=request.form.get('Total_expenditure')
    Diphtheria=request.form.get('Diphtheria')
    HIVAIDS=request.form.get('HIV/AIDS')
    GDP=request.form.get('GDP')
    Population=request.form.get('Population')
    thinness__1_19_years=request.form.get('thinness__1-19_years')
    thinness_5_9_years=request.form.get('thinness_5-9_years')
    Income_composition_of_resources=request.form.get('Income_composition_of_resources')
    Schooling = request.form.get('Schooling')

   
    life_ex = Life_Expectancy()

    result = life_ex.get_life_expect(Country,Year,Status, Adult_Mortality,
       infant_deaths, Alcohol, percentage_expenditure, Hepatitis_B,
       Measles, BMI, under_five_deaths,Polio,Total_expenditure,
       Diphtheria,HIVAIDS,GDP,Population,thinness__1_19_years,
       thinness_5_9_years,Income_composition_of_resources,Schooling)
    
    print("Result:", result)
    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5001,debug=False)