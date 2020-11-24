import sklearn
import pandas as pd
import numpy as np
import math
from os.path import expanduser as ospath
import matplotlib.pyplot as plt


def mutual_info():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1b.csv'))
    df = df.head(199)
    mutual_info_collection = []
    p_counter = []
    # calculate true mutual information
    alphabet = 'ABCDEFGHIJKLMNO'
    for i in alphabet:
        j = chr(ord(i)+1)
        while(j <= 'O'):
            counter = 0
            counter_col1 = df[i].sum()
            prob_col1_p1 = counter_col1/199
            prob_col1_p0 = 1 - prob_col1_p1
            i_col1_p1 = -prob_col1_p1 * math.log2(prob_col1_p1)
            i_col1_p0 = -prob_col1_p0 * math.log2(prob_col1_p0)
            counter_col2 = df[j].sum()
            prob_col2_p1 = counter_col2/199
            prob_col2_p0 = 1 - prob_col2_p1
            i_col2_p1 = -prob_col2_p1 * math.log2(prob_col2_p1)
            i_col2_p0 = -prob_col2_p0 * math.log2(prob_col2_p0)
            counter_x0y0 = 0
            counter_x0y1 = 0
            counter_x1y0 = 0
            counter_x1y1 = 0
            for x, y in df[[i, j]].itertuples(index=False):
                if x == 0 and y == 0:
                    counter_x0y0 += 1
                elif x == 0 and y == 1: 
                    counter_x0y1 += 1 
                elif x == 1 and y == 0: 
                    counter_x1y0 += 1
                elif x == 1 and y == 1: 
                    counter_x1y1 += 1
                else: 
                    pass
            px0y0 = counter_x0y0/199
            px0y1 = counter_x0y1/199
            px1y0 = counter_x1y0/199
            px1y1 = counter_x1y1/199
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
            mutual_info = i_col1_p1 + i_col1_p0 + i_col2_p1 + i_col2_p0 - i_total
            mutual_info_collection.append(mutual_info)
            print("tuple(", i, j,")", mutual_info)
            
            #permutation test
            total = 10
            for num in range(total):
                df2 = df.sample(n=60)
                col1_counter = 0
                for element in df2[i]:
                    if element == 1: 
                        col1_counter += 1
                p2x1 = col1_counter/total
                p2x0 = 1 - p2x1
                if p2x0 == 0:
                    i2_x0 == 0
                else: 
                    i2_x0 = -p2x0 * math.log2(p2x0)
                if p2x1 == 0: 
                    i2_x1 = 0
                else: 
                    i2_x1 = -p2x1 * math.log2(p2x1)
                col2_counter = 0
                for element in df2[j]:
                    if element == 1: 
                        col2_counter += 1
                p2y1 = col2_counter/total
                p2y0 = 1 - p2y1
                if p2y1 == 0: 
                    i2_y1 = 0
                else: 
                    i2_y1 = -p2y1 * math.log2(p2y1)
                if p2y0 == 0: 
                    i2_y0 = 0
                else: 
                    i2_y0 = -p2y0 * math.log2(p2y0)
                counter2_x0y0 = 0
                counter2_x0y1 = 0
                counter2_x1y0 = 0
                counter2_x1y1 = 0
                for x,y in df2[[i, j]].itertuples(index=False):
                    if x == 0 and y == 0:
                        counter2_x0y0 += 1
                    elif x == 0 and y == 1: 
                        counter2_x0y1 += 1 
                    elif x == 1 and y == 0: 
                        counter2_x1y0 += 1
                    elif x == 1 and y == 1: 
                        counter2_x1y1 += 1
                    else: 
                        pass
                p2x0y0 = counter2_x0y0/total
                p2x0y1 = counter2_x0y1/total
                p2x1y0 = counter2_x1y0/total
                p2x1y1 = counter2_x1y1/total
                if p2x0y0 == 0: 
                    i2x0y0 = 0
                else: 
                    i2x0y0 = -px0y0*math.log2(p2x0y0)
                if p2x0y1 == 0:
                    i2x0y1 = 0
                else: 
                    i2x0y1 = -px0y1*math.log2(p2x0y1)
                if p2x1y0 == 0: 
                    i2x1y0 = 0
                else: 
                    i2x1y0 = -p2x1y0*math.log2(p2x1y0)
                if p2x1y1 == 0: 
                    i2x1y1 = 0
                else: 
                    i2x1y1 = -p2x1y1*math.log2(p2x1y1)
                i2_total = i2x0y0 + i2x0y1 + i2x1y0 + i2x1y1
                mutual_info_2 = i2_x1 + i2_x0 + i2_y1 + i2_y0 - i2_total
                if mutual_info_2 < mutual_info: 
                    counter += 1
            p_value = (counter+1)/total
            p_counter.append(p_value)
            print("Tuple(",i,",",j,")", "p-value:", p_value)
            j = chr(ord(j)+1)
    x = []
    p_counter.sort()
    for i in range(105): 
        x.append(i)
    fig, ax = plt.subplots()
    ax.scatter(x,p_counter)
    ax.set_xlabel('index of observation')
    ax.set_ylabel('mutual information')
    ax.set_title("Scatter Plot for Mutual Information")
    plt.show()
    # p_counter.sort()
    # print(p_counter)
    # p_hb = []
    # for i in range(0, len(p_counter)):
    #     rank = i + 1
    #     if (rank/40)*0.1 == 0.1: 
    #         print("The index is: ", i)
    #     p_hb.append((rank/40)*0.1)
    # print(p_hb)

def jaccard_index():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1b.csv'))
    df = df.head(199)
    # calculate true mutual information
    alphabet = 'ABCDEFGHIJKLMNO'
    jcd_collection = []
    p_value_collection = []
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
            jcd_collection.append(jcd)
            # print("Tuple(",i,j,"), jaccard index: ", jcd)
            counter = 0
            nx0y1 = 0
            nx1y1 = 0
            nx1y0 = 0
            nx0y0 = 0
            for m in range(500): 
                df2 = df.sample(n=50)
                for x2, y2 in df2[[i, j]].itertuples(index=False):
                    if x2 == 0 and y2 == 1: 
                        nx0y1 += 1
                    elif x2 == 1 and y2 == 0: 
                        nx1y0 += 1
                    elif x2 == 1 and y2 == 1: 
                        nx1y1 += 1
                    else: 
                        nx0y0 += 1
                jcd2 = nx1y1/(nx0y1 + nx1y0 + nx1y1)
                if jcd2 > jcd: 
                    counter += 1
            p_value = (counter + 1)/501
            # if p_value < 0.023:
            #     print("(",i,j,")")
            p_value_collection.append(p_value)
            j = chr(ord(j)+1)
    p_value_collection.sort()
    p_counter = 0
    for i in range(len(p_value_collection)):
        if p_value_collection[i] < 0.05:
            p_counter+=1
    print("Without BH procedure: ", p_counter)
    adjusted_p_value = []
    x = []
    temp = []
    for i in range(105): 
        x.append(i+1)
    for j in range(len(p_value_collection)):
        adjusted_p_value.append((x[j]/105) * 0.05)
    for n in range(len(p_value_collection)):
        if(p_value_collection[n] < adjusted_p_value[n]):
            temp.append(p_value_collection[n])
    temp.sort(reverse=True)
    p_adjusted_counter = 0
    for i in range(len(p_value_collection)):
        if p_value_collection[i] < temp[0]:
            p_adjusted_counter +=1
    print("With BH procedure: ", p_adjusted_counter)
    print(temp[0])
            

    # x = []
    # for i in range(105): 
    #     x.append(i)
    # fig, ax = plt.subplots()
    # ax.scatter(x,p_value_collection)
    # ax.set_xlabel('index of observation')
    # ax.set_ylabel('p-value')
    # ax.set_title("Scatter Plot for Jaccard Index")
    # plt.show()

def chi_squared():
    df = pd.read_csv(ospath('/Users/ningjia/Desktop/CWRU/Junior (1st)/Data Analysis/Assignments/Assignment 3/data/p1b.csv'))
    total_num = 199
    df = df.head(199)
    alphabet = 'ABCDEFGHIJKLMNO'
    chi_list = []
    p_list = []
    p_value = 0
    for i in alphabet:
        j = chr(ord(i)+1)
        while(j <= 'O'):
            counter = 0
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
            e_x0y0 = (x0y0 + x0y1) * (x0y0 + x1y0)/total_num
            e_x0y1 = (x0y1 + x0y0) * (x0y1 + x1y1)/total_num
            e_x1y0 = (x1y0 + x1y1) * (x0y0 + x1y0)/total_num
            e_x1y1 = (x0y1 + x1y1) * (x1y0 + x1y1)/total_num
            chi_square = pow((x0y0 - e_x0y0),2)/e_x0y0 + pow((x0y1 - e_x0y1),2)/e_x0y1 + pow((x1y0 - e_x1y0),2)/e_x1y0 + pow((x1y1 - e_x1y1),2)/e_x1y1
            # print("Tuple(", i, j, "), chi squared = ", chi_square)
            chi_list.append(chi_square)

            # permutation test
            for m in range(500): 
                total = 500
                df2 = df.sample(n=50)
                k0l0 = 0
                k1l0 = 0
                k0l1 = 0
                k1l1 = 0
                for k, l in df2[[i, j]].itertuples(index=False):
                    if k == 0 and l == 1: 
                        k0l1 += 1
                    elif k == 1 and l == 0: 
                        k1l0 += 1
                    elif k == 1 and l == 1: 
                        k1l1 += 1
                    else: 
                        k0l0 += 1
                e_k0l0 = (k0l0 + k0l1) * (k0l0 + k1l0)/50
                e_k0l1 = (k0l1 + k0l0) * (k0l1 + k1l1)/50
                e_k1l0 = (k1l0 + k1l1) * (k0l0 + k1l0)/50
                e_k1l1 = (k0l1 + k1l1) * (k1l0 + k1l1)/50
                if (e_k0l0 == 0 or e_k0l1 == 0 or e_k1l0 == 0 or e_k1l1 == 0): 
                    total -= 1
                else: 
                    chi_square2 = pow((k0l0 - e_k0l0),2)/e_k0l0 + pow((k0l1 - e_k0l1),2)/e_k0l1 + pow((k1l0 - e_k1l0),2)/e_k1l0 + pow((k1l1 - e_k1l1),2)/e_k1l1
                if(chi_square2 >= chi_square): 
                    counter += 1
            p_value = (counter+1)/total
            p_list.append(p_value)
            if p_value <= 0.038: 
                print("Tuple(",i,",",j,")")
            j = chr(ord(j)+1)
    p_list.sort()
    adjusted_p_value = []
    temp = []
    x = []
    for i in range(105): 
        x.append(i+1)
    for j in range(len(p_list)):
        adjusted_p_value.append((x[j]/105) * 0.05)
    for n in range(len(p_list)):
        if(p_list[n] < adjusted_p_value[n]):
            temp.append(p_list[n])
    temp.sort(reverse=True)
    print(temp[0])
    p_counter = 0
    for i in range(len(p_list)): 
        if(p_list[i] >= temp[0]):
            p_counter += 1
    print(p_list)
    print(p_counter)
    # x = []
    # for i in range(105): 
    #     x.append(i)
    # fig, ax = plt.subplots()
    # ax.scatter(x, p_list)
    # ax.set_xlabel('index of observation')
    # ax.set_ylabel('p-value')
    # ax.set_title("Scatter Plot for Pearson\'s chi-squared")
    # plt.show()        


mutual_info()