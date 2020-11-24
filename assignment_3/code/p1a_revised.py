from sklearn.feature_selection import mutual_info_regression as mi_reg
import sklearn
import pandas as pd
import numpy as np
import math
from os.path import expanduser as ospath

def mutual_info():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1a.csv'))
    ret_val = sklearn.feature_selection.mutual_info_classif(df, df['O'], discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
    for(i = 0; ):
        
