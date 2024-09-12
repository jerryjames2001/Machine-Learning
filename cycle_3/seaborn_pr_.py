import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('./cycle_3/iris.csv')
sns.pairplot(df, kind='scatter')
sns.pairplot(df,kind='kde')
sns.pairplot(df,kind='hist')
sns.pairplot(df,kind='reg')
plt.show()