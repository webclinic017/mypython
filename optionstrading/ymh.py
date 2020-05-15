import numpy as np
import seaborn as sns
import basictools as bt
import optionsplay as op
sns.set(style="whitegrid")
import stockplay as sp
import pandas as pd
import csv


url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
content = pd.read_html(url)
stocklist = content[0]['Symbol'].tolist()


with open(r'ymh.csv','a') as fd:
    for t in l:
        if t[-1]!=0:
            writer=csv.writer(fd)
            writer.writerow([bt.get_data(0)]+t)






