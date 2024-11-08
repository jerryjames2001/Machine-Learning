import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris=pd.read_csv("./iris.csv")

sns.displot(iris['sepal.length'],kde=True,rug=True)
plt.title("Sepal length distribution")
plt.show()

sns.histplot(iris['sepal.width'],kde=True,bins=20)
plt.title("Histogram of sepal width")
plt.show()

sns.scatterplot(x="sepal.length", y="sepal.width", data=iris, hue="variety", style="variety")
plt.title("Sepal length vs Sepal width")
plt.show()