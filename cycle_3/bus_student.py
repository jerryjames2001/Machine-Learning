import matplotlib.pyplot as plt
import numpy as np

mode=np.array(["Walking","Cycling","Car","Bus","Train"])
freq=np.array([29,15,35,18,3])

plt.figure(figsize=(5,5))
plt.title("Jerry James \nMCA 23-25",loc="right")
plt.xlabel("Modes of transport")
plt.ylabel("Frequency")

plt.bar(mode,freq,width=0.2,color="lightblue")
plt.show()