import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

company = pd.read_csv('./Company_data.csv')
company.head()
company.describe()
company.info()
print("Feature value :")
x = company.iloc[:, :-1]
# print(x)
print("Target value :")
y = company.iloc[:, -1]
# print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
print("Intercept = ",regressor.intercept_)
print("coefficient = ",regressor.coef_)
y_pred = regressor.predict(x_test)
for (i,j) in zip(y_pred, y_test):
    if (i != j):
        print("Actual value : ",i,"Predicted value : ",j)
print("Number of mislabeled points from the test dataset :",(y_test != y_pred).sum())

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))