import numpy as np
import pandas as pd

old_data = pd.read_csv('../input/dataset_combined_old.csv')
new_data = pd.read_csv('../our_data/dataset_3.csv',usecols=[0,1,2,3,7])
combined_data = old_data.append(new_data)
combined_data.to_csv("../input/dataset_combined.csv")
old_data1 = pd.read_csv('../input/dataset_1_old.csv')
new_data1 = old_data1.append(new_data)
new_data1.to_csv("../input/dataset_1.csv")