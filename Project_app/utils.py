# Let's import required libraries and modules
import numpy as np
import pickle
import json
import config

# Let's create class for House_Price Prediction
class Boston_House():
    # Let's create constructor
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.CRIM = CRIM
        self.ZN = ZN
        self.INDUS = INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE = AGE
        self.DIS = DIS
        self.RAD = RAD
        self.TAX = TAX
        self.PTRATIO = PTRATIO
        self.B = B
        self.LSTAT = LSTAT
    
    def Load_Model(self):
        with open(config.MODEL_FILE_PATH_1,'rb') as fp:
            self.model = pickle.load(fp)
        with open(config.JSON_FILE_PATH,'r') as fj:
            self.json = json.load(fj)

    def Get_Price(self):
        self.Load_Model()

        #  Let's create test_array
        test_array = np.zeros(len(self.json['columns']))

        test_array[0] = self.CRIM 
        test_array[1] = self.ZN 
        test_array[2] = self.INDUS 
        test_array[3] = self.CHAS
        test_array[4] = self.NOX 
        test_array[5] = self.RM 
        test_array[6] = self.AGE 
        test_array[7] = self.DIS 
        test_array[8] = self.RAD 
        test_array[9] = self.TAX 
        test_array[10] = self.PTRATIO 
        test_array[11] = self.B 
        test_array[12] = self.LSTAT

        result = self.model.predict([test_array])
        return result