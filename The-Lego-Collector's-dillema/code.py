# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df=pd.read_csv(path)
X=df.drop(['list_price'],axis=1)
y=df['list_price']
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.3, random_state=6)
# code ends here



# --------------
import matplotlib.pyplot as plt
'''Let's check the scatter_plot for different features vs target variable list_price. This tells us which features are highly correlated with the target variable list_price and help us predict it better.
'''
# code starts here        
cols = X_train.columns

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20,20))

for i in range(0,3):
    for j in range(0,3): 
            col = cols[i*3 + j]
            axes[i,j].set_title(col)
            axes[i,j].scatter(X_train[col],y_train)
            axes[i,j].set_xlabel(col)
            axes[i,j].set_ylabel('list_price')
        

# code ends here
plt.show()


# --------------
'''Reduce feature redundancies!
Features highly correlated with each other adversely affect our lego pricing model. Thus we keep a inter-feature correlation threshold of 0.75. If two features are correlated and with a value greater than 0.75, remove one of them.'''
# Code starts here
corr=X_train.corr(method='pearson')
print(corr)
#We can see that the features of play_star_rating, val_star_rating and star_ratin have a correlation of greater than 0.75. We should drop two of these features to make our model better.

X_train.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)
X_test.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)


# Code ends here


# --------------
'''Is my price prediction ok?
Now let's come to the actual task, using linear regression to predict the price. We will check the model accuracy using r^2 score and mse (If model is bad, please keep extra money for the sets!).'''
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
#Instantiate a linear regression model with LinearRegression() and save it to a variable called 'regressor'.
regressor=LinearRegression()
#fit model on trining data
regressor.fit(X_train,y_train)
#predictions
y_pred=regressor.predict(X_test)
print(y_pred)
#mean squared_error
mse=mean_squared_error(y_test,y_pred)
print("mean squared error",mse)
# R-square calculation
r2=r2_score(y_test,y_pred)
print(' R-square',r2)


# Code ends here


# --------------
# Code starts here
residual=(y_test - y_pred)
print(residual)
residual.plot.hist()
plt.show()



# Code ends here


