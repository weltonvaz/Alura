import pandas as pd
import numpy as np

carros = pd.read_csv('Auto.csv',sep =',')
print(carros['horsepower'])