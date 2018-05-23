import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import pandas as pd
 
style.use('fivethirtyeight')
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
    graph_data=open('samplefile.txt','r').read()
    print(str(graph_data))
    lines=graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines[-20:]:
        if len(line)>1:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)

ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()









# Data
#df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21) })
  
# multiple line plot
#plt.plot( 'x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
#plt.plot( 'x', 'y2', data=df, marker='', color='olive', linewidth=2)
#plt.plot( 'x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
#plt.legend()

