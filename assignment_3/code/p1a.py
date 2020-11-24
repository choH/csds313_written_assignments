import pandas as pd
import numpy as np
import math
from os.path import expanduser as ospath
from sklearn.feature_selection import mutual_info_regression as mi_reg
import sklearn

def a_mutual_info():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1a.csv'))
    #count_xy = df.sum() //X = 1 : 50, Y = 1 : 21
    #sample_num = df.shape[0] //total num of random variables: 199
    px1 = 50/199
    px0 = 1 - px1
    i_x1 = -px1 * math.log2(px1)
    i_x0 = -px0 * math.log2(px0)
    py1 = 21/199
    py0 = 1 - py1
    i_y1 = -py1 * math.log2(py1)
    i_y0 = -py0 * math.log2(py0)
    counter_x0y0 = 0
    counter_x0y1 = 0
    counter_x1y0 = 0
    counter_x1y1 = 0
    for row in df.itertuples():
        if row.X == 0 and row.Y == 0:
            counter_x0y0 += 1
        elif row.X == 0 and row.Y == 1: 
            counter_x0y1 += 1 
        elif row.X == 1 and row.Y == 0: 
            counter_x1y0 += 1
        elif row.X == 1 and row.Y == 1: 
            counter_x1y1 += 1
        else: 
            return
    px0y0 = counter_x0y0/199
    px0y1 = counter_x0y1/199
    px1y0 = counter_x1y0/199
    px1y1 = counter_x1y1/199 #0
    # print("X0Y0: ", px0y0, "X0Y1: ", px0y1, "X1Y0: ", px1y0, "X1Y1: ", px1y1)
    i_x0y0 = -px0y0 * math.log2(px0y0)
    i_x0y1 = -px0y1 * math.log2(px0y1)
    i_x1y0 = -px1y0 * math.log2(px1y0)
    i_x1y1 = 0
    print("X0Y0: ", i_x0y0, "X0Y1: ", i_x0y1, "X1Y0: ", i_x1y0, "X1Y1: ", i_x1y1)
    print("Total: ", i_x0y0 + i_x0y1 + i_x1y0 + i_x1y1)

def mutual_info_permutation():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1a.csv'))
    counter = 0
    for i in range(200):
        df2 = df.sample(n=40)
        x1_counter = 0
        for element in df2['X']:
            if element == 1: 
                x1_counter += 1
        px1 = x1_counter/40
        px0 = 1 - px1
        i_x1 = -px1 * math.log2(px1)
        i_x0 = -px0 * math.log2(px0)
        y1_counter = 0
        for element in df2['Y']:
            if element == 1: 
                y1_counter += 1
        py1 = y1_counter/40
        py0 = 1 - py1
        if py1 == 0: 
            i_y1 = 0
        else: 
            i_y1 = -py1 * math.log2(py1)
        if py0 == 0: 
            i_y0 = 0
        else: 
            i_y0 = -py0 * math.log2(py0)
        counter_x0y0 = 0
        counter_x0y1 = 0
        counter_x1y0 = 0
        counter_x1y1 = 0
        for row in df2.itertuples():
            if row.X == 0 and row.Y == 0:
                counter_x0y0 += 1
            elif row.X == 0 and row.Y == 1: 
                counter_x0y1 += 1 
            elif row.X == 1 and row.Y == 0: 
                counter_x1y0 += 1
            elif row.X == 1 and row.Y == 1: 
                counter_x1y1 += 1
            else: 
                return
        px0y0 = counter_x0y0/40
        px0y1 = counter_x0y1/40
        px1y0 = counter_x1y0/40
        px1y1 = counter_x1y1/40
        if px0y0 == 0: 
            ix0y0 = 0
        else: 
            ix0y0 = -px0y0*math.log2(px0y0)
        if px0y1 == 0:
            ix0y1 = 0
        else: 
            ix0y1 = -px0y1*math.log2(px0y1)
        if px1y0 == 0: 
            ix1y0 = 0
        else: 
            ix1y0 = -px1y0*math.log2(px1y0)
        if px1y1 == 0: 
            ix1y1 = 0
        else: 
            ix1y1 = -px1y1*math.log2(px1y1)
        i_total = ix0y0 + ix0y1 + ix1y0 + ix1y1
        mutual_info = i_x1 + i_x0 + i_y1 + i_y0 - i_total
        if mutual_info >= 0.046993161946257356: 
            counter += 1
        print("num of permutation: ", i, ", mutual information: ",mutual_info)
    print("num of more significant value: ", counter)

def jaccard_index(): 
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1a.csv'))
    x1y1 = 0
    x0y1 = 0
    x1y0 = 0
    x0y0 = 0
    counter = 0
    for i in range(200):
        df2 = df.sample(n=40)
        for row in df2.itertuples():
            if row.X == 0 and row.Y == 1: 
                x0y1 += 1
            elif row.X == 1 and row.Y == 0: 
                x1y0 += 1
            elif row.X == 1 and row.Y == 1: 
                x1y1 += 1
                print("hasjdhkashjdk")
            else: 
                x0y0 += 1
        jcd = x1y1/(x0y1+x1y0+x1y1)
        if jcd > 0.0: 
            counter += 1
        print("Jaccard Index for data: ", jcd)
    print("num of more significant value: ", counter)

def chi_squared():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1a.csv'))
    total_num = 199
    x1y1 = 0
    x0y1 = 0
    x1y0 = 0
    x0y0 = 0
    for row in df.itertuples():
        if row.X == 0 and row.Y == 1: 
            x0y1 += 1
        elif row.X == 1 and row.Y == 0: 
            x1y0 += 1
        elif row.X == 1 and row.Y == 1: 
            x1y1 += 1
            print("hasjdhkashjdk")
        else: 
            x0y0 += 1
    e_x0y0 = (x0y0 + x0y1) * (x0y0 + x1y0)/total_num
    e_x0y1 = (x0y1 + x0y0) * (x0y1 + x1y1)/total_num
    e_x1y0 = (x1y0 + x1y1) * (x0y0 + x1y0)/total_num
    e_x1y1 = (x0y1 + x1y1) * (x1y0 + x1y1)/total_num
    chi_square = pow((x0y0 - e_x0y0),2)/e_x0y0 + pow((x0y1 - e_x0y1),2)/e_x0y1 + pow((x1y0 - e_x1y0),2)/e_x1y0 + pow((x1y1 - e_x1y1),2)/e_x1y1
    print(chi_square)

def test():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1a.csv'))
    ret_val = sklearn.feature_selection.mutual_info_classif(df, df['X'], discrete_features='auto', copy=True, random_state=None)
    print(ret_val)

a_mutual_info()