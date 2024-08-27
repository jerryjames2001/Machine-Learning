import matplotlib.pyplot as plt
day=["mon","tues","wed","thurs","fri"]
drinks=[300,450,150,400,650]
food=[400,500,350,300,500]
fig, axis=plt.subplots(2,1,figsize=(10,8))

axis[0].plot(day,drinks,color="cyan",marker="h",linestyle="--",markersize=10,markerfacecolor="magenta",markeredgecolor="black")
axis[0].set_xlabel("Days")
axis[0].set_ylabel("Drinks")
axis[0].set_title("Sales Data 1",loc="right")
axis[0].set_title("Jerry James \n MCA 23-25",loc="left")
axis[0].grid(True,color="blue",linestyle="dotted")


axis[1].set_title("Sales Data 2",loc="right")
axis[1].plot(day,food,color="yellow",marker="D",linestyle="-",markerfacecolor="green",markeredgecolor="red")
axis[1].set_xlabel("Days")
axis[1].set_ylabel("Food")
axis[1].grid(True,color="blue",linestyle="dotted")
plt.show()