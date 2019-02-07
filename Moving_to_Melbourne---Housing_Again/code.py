# --------------
'''Data loading and spliting
The first step -load the dataset and see how it looks like. Additionally, split it into train and test set.'''
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path
df=pd.read_csv(path)
print(df.head())
#Code starts here
#features
X=df.drop(['Price'],axis=1)
#target
y=df['Price']
#Split the dataframe into X_train,X_test,y_train,y_test
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size = 0.3,random_state = 6)
#Find the correlation between the features which are stored in 'X_train'
corr=X_train.corr(method='pearson')
print('correlation between features-',corr)


# --------------
'''Prediction using Linear regression
Now let's come to the actual task, using linear regression to predict the price of the house. We will check the model performance using r^2 score.'''
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Code starts here
#Instantiate linear regression model 
regressor=LinearRegression()
#fit model on training data
regressor.fit(X_train,y_train)
#Make predictions on the test features
y_pred=regressor.predict(X_test)
print('predictions on test features-',y_pred)
#Find the r^2 score for checking the model performance.
r2=r2_score(y_test,y_pred)
print('r^2 score=',r2)


# --------------
'''Prediction using Lasso
In this task let's predict the price of the house using a lasso regressor. Check if there is any improvement in the prediction.'''
from sklearn.linear_model import Lasso

# Code starts here
#Instantiate a lasso model 
lasso=Lasso()
#fit model on training data
lasso.fit(X_train,y_train)
#make predictions on test features
lasso_pred=lasso.predict(X_test)
print('lasso test features predictions-',lasso_pred)
#Find the r^2 score
r2_lasso=r2_score(y_test,lasso_pred)
print('r^2 score lasso=',r2_lasso)


# --------------
from sklearn.linear_model import Ridge

# Code starts here
ridge=Ridge()
ridge.fit(X_train,y_train)
ridge_pred=ridge.predict(X_test)
print(ridge_pred)
r2_ridge=r2_score(y_test,ridge_pred)
print(r2_ridge)


# Code ends here


# --------------
'''Prediction using cross validation
Now let's predict the house price using cross-validated estimators which is the part of the Model selection: choosing estimators and their parameters.'''
from sklearn.model_selection import cross_val_score

#Code starts here
#Initiate a LinearRegression
regressor=LinearRegression()
#Calculate the cross_val_score on X_train,y_train having model = regressor and cv = 10
score=cross_val_score(regressor, X_train, y_train, cv=10)
print('cv score-',score)
#Calculate the mean of cross_val_score
mean_score=score.mean()
print('mean of cv score=',mean_score)


# --------------
'''Prediction using polynomial regressor
As you can see that there is very less improvement(~1%) even after applying regularization and cross-validation score. Now let's perform the prediction using a polynomial regressor to generate 2nd degree polynomial features.'''
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#Code starts here
#Initiate pipeline for polynomial features
model=make_pipeline(PolynomialFeatures(2),LinearRegression())
#Fit the model on the training data
model.fit(X_train,y_train)
#Make predictions on the test features 
y_pred=model.predict(X_test)
print('predicted values-',y_pred)
#Find the r^2 score
r2_poly=r2_score(y_test,y_pred)
print('r^2 score poly=',r2_poly)


