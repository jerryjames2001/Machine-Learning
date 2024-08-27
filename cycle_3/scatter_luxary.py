import matplotlib.pyplot as plt
import numpy as np

months=np.array(["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])
aff_seg=np.array([173,153,195,147,120,144,148,109,174,130,172,131])
lux_seg=np.array([189,189,105,112,173,109,151,197,174,145,177,161])
sup_lux_seg=np.array([185,185,126,134,196,153,112,133,200,145,167,110])

plt.subplots(figsize=(7,6))
plt.xlabel("Months",fontsize=18)
plt.ylabel("Sales of segments")
plt.title("Sales data")
plt.title("Jerry James \nMCA 23-25",loc="right")

plt.scatter(months,aff_seg,label="Affordable segment",color="pink")
plt.scatter(months,lux_seg,label="Luxury segment",color="red")
plt.scatter(months,sup_lux_seg,label="Super Luxury Segment",color="blue")

plt.show()