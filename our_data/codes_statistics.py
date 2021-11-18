import numpy as np
import pandas as pd

def break_out_codes(code):
    code = str(code).replace('-','9')
    codes = list(code)
    scores = np.zeros(9)
    for c in codes:
        c = int(c)
        scores[c-1] = 1
    return scores


codes = pd.read_csv("input/dataset_combined.csv", usecols=['Codes with >= 2 votes'])
codes = codes.applymap(break_out_codes)
codes['What'] = codes['Codes with >= 2 votes'].str[0]
codes['Why'] = codes['Codes with >= 2 votes'].str[1]
codes['How'] = codes['Codes with >= 2 votes'].str[2]
codes['When'] = codes['Codes with >= 2 votes'].str[3]
codes['Who'] = codes['Codes with >= 2 votes'].str[4]
codes['References'] = codes['Codes with >= 2 votes'].str[5]
codes['Contribution'] = codes['Codes with >= 2 votes'].str[6]
codes['Other'] = codes['Codes with >= 2 votes'].str[7]
codes['Exclusion'] = codes['Codes with >= 2 votes'].str[8]
codes = codes.drop(columns='Codes with >= 2 votes')
code_counts = codes.sum(axis=1)

means = codes.mean()
means = means.map(lambda x: "{:.1f}".format(x*100) + "%")
print('Distribution of README Categories')
print(codes.sum())

print('\nPercentages of README Categories')
print(means)

print('\nNumber of Codes per Section')
print(code_counts.value_counts())