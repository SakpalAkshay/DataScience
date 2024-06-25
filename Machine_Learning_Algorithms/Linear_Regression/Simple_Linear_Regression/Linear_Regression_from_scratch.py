import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
df = pd.read_csv('placement.csv')

class MyLinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None
    
    def fit(self,X_train,y_train):
        numerator = 0
        denominator = 0
        
        #just as mentioned in notes we will calculate our slope and intercept values
        for i in range(X_train.shape[0]): #for summing up all values we use a loop
            numerator = numerator + ((X_train[i] - X_train.mean())*(y_train[i] - y_train.mean()))
            denominator = denominator + ((X_train[i] - X_train.mean())*(X_train[i] - X_train.mean()))
            
        self.slope = numerator / denominator
        self.intercept = y_train.mean() - (self.slope * X_train.mean())
        
        print(self.slope)
        print(self.intercept)
     
    def predict(self,X_test):
        
        print(X_test)
        # y = mx + b
        return self.slope * X_test + self.intercept


#train test split and prediction
X = df.iloc[:,0].values
y = df.iloc[:,-1].values

#splitting data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)
lr = MyLinearRegression()
lr.fit(X_train,y_train)

# slope = 0.5579519734250721
# intercept -0.8961119222429152

print(lr.predict(X_test[0]))

#8.58
#3.891116009744203


#Compare this o/p with our LR model using Sklearn in other file both are same
