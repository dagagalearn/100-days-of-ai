import  matplotlib.pyplot as plt
import numpy as np
figure, axes = plt.subplots(3,2)
x = np.linspace(0,2*np.pi,1000)

sin_x = np.sin(x)
cos_x = np.cos(x)
tan_x = np.tan(x)

sin_x[sin_x==0]=np.nan
cos_x[cos_x==0]=np.nan
tan_x[np.abs(tan_x)>=10]=np.nan
tan_x[tan_x==0]=np.nan


csc_x = 1/np.sin(x)
sec_x = 1/np.cos(x)
cot_x = 1/np.tan(x)


axes[0,0].plot(x, sin_x,color="green")
axes[0,0].set_title("Graph of sin(x)")

axes[0,1].plot(x,cos_x,color="#131A14")
axes[0,1].set_title("Graph of cos(x)")

axes[1,0].plot(x,tan_x,color="red")
axes[1,0].set_title("Graph of tan(x)")

axes[1,1].plot(x,csc_x,color="blue")
axes[1,1].set_title("Graph of csc(x)")

axes[2,0].plot(x,sec_x,color="black")
axes[2,0].set_title("Graph of sec(x)")

axes[2,1].plot(x,cot_x,color="#03fca5")
axes[2,1].set_title("Graph of cot(x)")

for ax in axes.flat:
    ax.set_ylim(-5,5)
    ax.grid(True)

plt.tight_layout()

plt.show()
