# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(path)


#Code starts here
data['Rating'].plot.hist()
plt.show()
data=data[data['Rating']<=5]
data['Rating'].plot.hist()
plt.show()
#Code ends here


# --------------
# code starts here
total_null=data.isnull().sum()
percent_null=total_null/data.isnull().count()
missing_data=pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)
data=data.dropna()
total_null_1=data.isnull().sum()
percent_null_1=total_null_1/data.isnull().count()
missing_data_1=pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)

# code ends here


# --------------
'''Category vs Rating
Let's first check if category and ratings have any sort of relation'''
#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box",height=10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())
data['Installs']=data['Installs'].str.replace('+','').str.replace(',','') 
data['Installs']=data['Installs'].astype(int)

le=LabelEncoder()
data['Installs']=le.fit_transform(data['Installs'])
sns.regplot(x="Installs", y="Rating",data=data)
plt.title('Rating vs Installs [RegPlot]')
#Code ends here



# --------------
#Price vs Ratings
#Code starts here
#Print value counts of Price column
print(data['Price'].value_counts())

#Remove dollar sign from Price column
data['Price']=data['Price'].str.replace('$','')

#Convert the Price column to datatype float
data['Price']=data['Price'].astype(float)

#plotting the regression line.
sns.regplot(x="Price", y="Rating",data=data)
plt.title('Rating vs Price [RegPlot]')

#Code ends here


# --------------
#Genre vs Rating
#Code starts here
#unique values of the column Genres
print(data['Genres'].unique())

# Split the values of column Genres by ;
data['Genres']=data['Genres'].str.split(';').str[0]

#Group Genres and Rating
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

#Sort the values
gr_mean=gr_mean.sort_values(by=['Rating'])

#Print the first and last value of gr_mean
print('First value=',gr_mean.head(1))
print('Last value=',gr_mean.tail(1))
#Code ends here


# --------------
#Last Updated vs Rating
#Code starts here
#Print and visualise the values of Last Updated column of 'data'
print(data['Last Updated'])

#Convert Last Updated to datetime format
data['Last Updated'] =  pd.to_datetime(data['Last Updated'])

#Find out the max value in Last Updated column 
max_date=data['Last Updated'].max()

#Create new column Last Updated Days which is the difference between max_date and values of column Last Updated in days using "dt.days" function
data['Last Updated Days']= max_date-data['Last Updated']
data['Last Updated Days']=data['Last Updated Days'].dt.days

#plot the regression line for Rating vs Last Updated [RegPlot]
plt.figure(figsize = (10,10)) 
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title("Rating vs Last Updated [RegPlot]")
plt.show()
#Code ends here


