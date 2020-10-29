# Importing liberaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing Datasets
dataset = pd.read_csv('Python/Data.csv')

# Seperating dependent and independent vairiable
# Independent vairiable
x = dataset.iloc[:,:-1].values

#Dependent vairible
y = dataset.iloc[:,3].values