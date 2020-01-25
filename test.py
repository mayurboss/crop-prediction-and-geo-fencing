import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# from sklearn.linear_model import LogisticRegression
data = pd.read_csv("agree.csv")
print("\nDisplay the Key ")
print(list(data))

print("\nDisplay the Row and Column")
print(data.shape)

print("\nDisplay the All Data present in Dataset")
print(data.describe)
# print("hello eorld")

data.head()

#for compare total cost and earning
data.plot(x='Earning', y='totalcost', style='o')
plt.title('Earning vs totalcost')
plt.xlabel('Earning')
plt.ylabel('totalcost')
plt.show()


#for
plt.figure(figsize=(100,100))
plt.tight_layout()
seabornInstance.distplot(data['Earning'])



'''this is conversion str to int'''
file_handler = open("agree.csv", "r")

# creating a Pandas DataFrame
# using read_csv function
# that reads from a csv file.
data = pd.read_csv(file_handler, sep = ",")

# closing the file handler
file_handler.close()

# creating a dict file
Crop = {'ARHAR': 1,'COTTON': 2,'GRAM': 3,'GROUNDNUT': 4,'MAIZE': 5,'OILSEEDS': 6,'RICE': 7,'SUGARCANE': 8,'WHEAT': 9,'MOONG': 10}
answerclass = {'ARHAR': 1,'COTTON': 2,'GRAM': 3,'GROUNDNUT': 4,'MAIZE': 5,'OILSEEDS': 6,'RICE': 7,'SUGARCANE': 8,'WHEAT': 9,'MOONG': 10}
State = {'Uttar Pradesh': 101,'Karnataka': 102,'Gujarat': 103,'Andhra Pradesh': 104,'Maharashtra': 105,'Punjab': 106,
         'Tamil Nadu': 107,'Bihar': 108,'Orissa': 109,'West Bengal': 110,
         'Madhya Pradesh': 111,'Rajasthan': 112,'Haryana':113}
#
# # traversing through dataframe
# Gender column and writing
# values where key matches
data.Crop = [Crop[item] for item in data.Crop]
print(data)


data.answerclass = [answerclass[item] for item in data.answerclass]
print(data)

data.State = [State[item] for item in data.State]
print(data)
'''this is conversion str to int'''



# X = data[['Crop']['State']['2018-19']['Earning']['totalcost']]
# y = data['answerclass']
X = data['Earning'].values.reshape(-1,1)
y = data['answerclass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train) #training the algorithm

#To retrieve the intercept:
print(regressor.intercept_)
#For retrieving the slope:
print(regressor.coef_)


y_pred = regressor.predict(X_test)

plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()

print(Crop)