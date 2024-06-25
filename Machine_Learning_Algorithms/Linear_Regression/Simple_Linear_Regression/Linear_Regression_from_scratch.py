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
