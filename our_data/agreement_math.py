import pandas as pd
import numpy as np

def break_out_codes(code):
    code = str(code).replace('-','9')
    codes = list(code)
    scores = np.zeros(9)
    for c in codes:
        c = int(c)
        scores[c+1] = 1
    return scores

def calcPctAgreement(df):
    codes = df.iloc[:,4:7]
    codes['kd-agree'] = np.where(codes['code-khoi'] == codes['code-david'],1,0)
    codes['ke-agree'] = np.where(codes['code-khoi'] == codes['code-evan'],1,0)
    codes['de-agree'] = np.where(codes['code-evan'] == codes['code-david'],1,0)
    codes['total-agree'] = (codes['kd-agree'] + codes['ke-agree'] + codes['de-agree'])/3.0
    return codes['kd-agree'].mean(), codes['ke-agree'].mean(), codes['de-agree'].mean(), codes['total-agree'].mean()


ourdata = pd.read_csv("our_data/612 README - dataset_3.csv")


mini_df = ourdata.head(10)
kd, ke, de, t = calcPctAgreement(ourdata)
print("Khoi-David Agreement: {:.1f}%\nKhoi-Evan Agreement: {:.1f}%\nDavid-Evan Agreement: {:.1f}%\nTotal Agreement: {:.1f}%".format(kd*100,ke*100,de*100,t*100))


