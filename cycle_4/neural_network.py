import pandas as pd
import tensorflow
import matplotlib.pyplot as plt
df = pd.read_csv('./housepricedata.csv')
print(df.head())
dataset = df.values
X = dataset[:,0:10]
Y = dataset[:,10]

from sklearn import preprocessing
min_max_scalar = preprocessing.MinMaxScaler()
x_scale = min_max_scalar.fit_transform(X)
print(x_scale)

from sklearn.model_selection import train_test_split
x_train, x_val_and_test, y_train, y_val_and_test = train_test_split(x_scale,Y,test_size=0.3)

x_val, x_test, y_val, y_test = train_test_split(x_val_and_test,y_val_and_test,test_size=0.5)

print(x_train.shape, x_val.shape, x_test.shape, y_train.shape, y_val.shape, y_test.shape)

from keras.models import Sequential
from keras.layers import Dense
model = Sequential([Dense(32, activation='relu',input_shape=(10,)),
                    Dense(32, activation='relu'),
                    Dense(1, activation='sigmoid'),])
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
hist = model.fit(x_train, y_train,
                 batch_size=32, epochs=100,
                 validation_data=(x_val, y_val))
model.evaluate(x_test, y_test)[1]

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss')
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend(['train','val'],loc='upper right')
plt.show()