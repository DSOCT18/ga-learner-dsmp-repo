# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
#Load dataset in a dataframe data.
data= pd.read_csv(path)
#Save the value counts of Loan_Status in a variable called loan_status
loan_status= data['Loan_Status'].value_counts()
#Plot a bar graph of loan_status
loan_status.plot(kind='bar')
#labeling
plt.xlabel('Loan_Status')
plt.ylabel('Counts')
plt.title('Company has more loan approvals or loan disapprovals?')
plt.show()


# --------------
#Code starts here
#Groupby the columns Property_Area and Loan_Status
property_and_loan= data.groupby(['Property_Area','Loan_Status'])
property_and_loan= property_and_loan.size().unstack()
#Plotting unstacked bar plot
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
#Rotate the x-labels by 45 degrees using plt.xticks
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
"""plotting a graph for Education and Loan Status"""

#Groupby Education and Loan_Status and store it in a variable called 'education_and_loan'
education_and_loan= data.groupby(['Education','Loan_Status'])
education_and_loan= education_and_loan.size().unstack()
#plot stacked bar graph
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()



# --------------
#Code starts here
#Create a subset of dataframe 'data' as 'graduate' which only has Education=Graduate.
graduate= data[data['Education'] == 'Graduate']
#Create a subset of dataframe 'data' as 'not_graduate' which only has Education=Not_Graduate.
not_graduate= data[data['Education'] == 'Not Graduate']
#Plot a density plot LoanAmount of 'graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')
#Plot a density plot LoanAmount of 'not_graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')












#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
#Create three subplots with (nrows = 3 , ncols = 1)
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1)
#plot scatter plot between 'ApplicantIncome' and LoanAmount
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')
#Plot scatter plot between 'CoapplicantIncome' and LoanAmount
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')
#Create a new column in the dataframe called 'TotalIncome' which is a sum of the values of columns ApplicantIncome and CoapplicantIncome
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
#Plot scatter plot between 'ApplicantIncome' and LoanAmount
ax_3.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_3.set_title('TotalIncome')


