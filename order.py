#%%
import numpy as np
import cv2
import pandas as pd
#%%
df = pd.read_csv('dataX.csv')

df2 = df.dropna()