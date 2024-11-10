import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix

dataset = pd.read_csv("./Blood_Transfusion.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20)

classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print(classification_report(y_test,y_pred))