import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

help(signal.buttord)
# signal.buttord()



# 设置x,y轴的数值
x1 = np.linspace(0, 15, 200)
y1 = np.sin(x1)
y2 = np.cos(x1)

# 在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
plt.plot(x1, y1, label="$sin(x)$", color="blue", linewidth=4)
plt.plot(x1, y2, label="$cos(x)$", color="red", linewidth=4)
#
plt.show()



