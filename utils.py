import numpy as np
import pandas as pd
import pickle
import config 
import json

#from sklearn.preprocessing import LabelEncoder
class Life_Expectancy():
    def __init__(self):
        pass

    def __load_data(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.COLUMN_DATA_JSON, 'r') as f:
            self.col_data = json.load(f)

        self.col_names = self.model.feature_names_in_
 

    def get_life_expect(self,Country,Year,Status, Adult_Mortality,
        infant_deaths, Alcohol, percentage_expenditure, Hepatitis_B,
        Measles, BMI, under_five_deaths,Polio,Total_expenditure,
        Diphtheria,HIVAIDS,GDP,Population,thinness__1_19_years,
        thinness_5_9_years,Income_composition_of_resources,Schooling):

        self.__load_data() 
        
        
        Country_index = np.where(self.col_names == 'Country_'+ Country)[0]
        # print("region_index",region_index)

        Status = self.col_data['Status'][Status]
        

        test_array = np.zeros((1,self.model.n_features_in_))
        test_array[0,Country_index] = 1
        test_array[0,1] = Year
        test_array[0,2] = Status
        test_array[0,3] = Adult_Mortality
        test_array[0,4] = infant_deaths
        test_array[0,5] = Alcohol
        test_array[0,6] = percentage_expenditure
        test_array[0,7] = Hepatitis_B
        test_array[0,8] = Measles
        test_array[0,9] = BMI
        test_array[0,10] = under_five_deaths
        test_array[0,11] = Polio
        test_array[0,12] = Total_expenditure
        test_array[0,13] = Diphtheria
        test_array[0,14] = HIVAIDS
        test_array[0,15] = GDP
        test_array[0,16] = Population
        test_array[0,17] = thinness__1_19_years
        test_array[0,18] = thinness_5_9_years
        test_array[0,19] = Income_composition_of_resources
        test_array[0,20] = Schooling


        predicted_res = self.model.predict(test_array)
        print("predicted_result :",predicted_res)

        return predicted_res

