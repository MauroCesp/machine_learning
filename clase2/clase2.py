import scipy
import numpy as np
import matplotlib
import pandas as pd

df = pd.read_csv("indian_liver_patient.csv")

print(df.head())
print(df.describe())

#---------- Identificar desequilibrio de clases ------------

class_distribution = df.groupby('Dataset').size()
print(class_distribution)

#------- Correlacion de atributos--------------
# NO dice la corelacion entre los atributos


pd.set_option('display_width', 1000)
pd.set_option('precision', 3)

print(df.corr())
