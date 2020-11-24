import sklearn
import pandas as pd
import numpy as np
import math
from os.path import expanduser as ospath
import matplotlib.pyplot as plt

df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1b.csv'))
df = df.head(199)

def ji():
    alphabet = 'ABCDEFGHIJKLMNO'
    true_ji = []
    p = []
    for i in alphabet:
        j = chr(ord(i)+1)
        while(j <= 'O'):
            x1y1 = 0
            x0y1 = 0
            x1y0 = 0
            x0y0 = 0
            for x, y in df[[i, j]].itertuples(index=False):
                if x == 0 and y == 1: 
                    x0y1 += 1
                elif x == 1 and y == 0: 
                    x1y0 += 1
                elif x == 1 and y == 1: 
                    x1y1 += 1
                else: 
                    x0y0 += 1
            jcd = x1y1/(x0y1+x1y0+x1y1)
            true_ji.append(jcd)
            print("(",i, j, ")", jcd)

            # permutation test
            total = 500
            counter = 0
            for m in range(total):
                df2 = df.sample(n=50)
                m1n1 = 0
                m0n1 = 0
                m1n0 = 0
                m0n0 = 0
                for x2, y2 in df2[[i, j]].itertuples(index=False):
                    if x2 == 0 and y2 == 1: 
                        m0n1 += 1
                    elif x2 == 1 and y2 == 0: 
                        m1n0 += 1
                    elif x2 == 1 and y2 == 1: 
                        m1n1 += 1
                    else: 
                        m0n0 += 1
                if (m1n0+m0n1+m1n1) == 0: 
                    total -= 1
                else: 
                    jcd2 = m1n1/(m1n0+m0n1+m1n1)
                if jcd2 < jcd: 
                    counter += 1
            p_value = (counter + 1)/(total + 1)
            print("p:", p_value)
            p.append(p_value)
            j = chr(ord(j)+1)
    p.sort()     
    x = []
    for i in range(105): 
        x.append(i)
    bh_counter = 0
    for i in range(len(p)): 
        if p[i] < 0.05: 
            bh_counter += 1
    print("Without BH: ", bh_counter)
    x = []
    adjusted = []
    temp = []
    for i in range(105): 
        x.append(i+1)
    for j in range(len(p)):
        adjusted.append((x[j]/105) * 0.05)
    for n in range(len(p)):
        if(p[n] < adjusted[n]):
            temp.append(p[n])
    temp.sort(reverse=True)
    print(adjusted)
    print(p)
    # print("largest: ", temp[0])
    # bh = 0
    # for i in range(len(p)):
    #     if(p[n] > temp[0]): 
    #         bh += 1
    # print("With BH: ", bh)
    # fig, ax = plt.subplots()
    # ax.scatter(x,p)
    # ax.set_xlabel('index of observation')
    # ax.set_ylabel('p-value')
    # ax.set_title("Scatter Plot for Jaccard Index")
    # plt.show()


ji()