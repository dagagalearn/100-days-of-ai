import matplotlib.pyplot as plt
import numpy as np
days = np.array(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
temp = np.array([20,21,23,24,25,28,29])

line_style = dict()
plt.title("Temprature of the days of the week",fontsize=30,color="blue",font="Arial")
plt.plot(days,temp,color="red",
         marker=".",
         markersize=10)
plt.xlabel("Days")
plt.ylabel("Temprature")
plt.show()
