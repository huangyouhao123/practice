# -*- coding: gbk -*-
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

path="E:\pythonproject4\pachong\weather.xlsx"
data=pd.read_excel(path)
data['�����'] = data['�����'].apply(lambda x: int(float(x[0:-1])) if len(x) > 0 else 0)
data['�����'] = data['�����'].apply(lambda x: int(float(x[0:-1])) if len(x) > 0 else 0)
length=len(data)
x=np.arange(length)
y1=np.array(data["�����"])
y2=np.array(data["�����"])
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()