import matplotlib.pyplot as plt
years=[2001,2002,2003,2004,2005,2006,2007]
car_value=[24000,22500,19700,17500,14500,10000,5800]

plt.figure(figsize=(10,6))

plt.subplot(111)
plt.plot(years, car_value,color='red',marker="*",linestyle="-.",markersize=20,markerfacecolor='green')     
plt.title('Jerry James \n MCA 23-25',loc='right')
plt.title('value deprication',loc='left')
plt.xlabel('Years')
plt.ylabel('Car Value')

plt.show()