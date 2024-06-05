import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ddf = pd.read_csv(r'C:\Users\kliker\Desktop\dataset_209770_6.txt', sep=' ')
pd.set_option('display.max_columns', None)

# aggregate(['sucrose', 'alanin', 'citrate', 'glucose', 'oleic_acid'], 'mean')


plot = sns.lmplot(x='glucose', y='alanin', data=ddf)
plot.savefig("out.png")
