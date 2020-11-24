import sklearn
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import itertools
import json

df = pd.read_csv('assignment_3/data/p1b.csv', header=None)


# The below method is borrowed from lyx on https://stackoverflow.com/a/24826348
def compute_MI(x, y):
    sum_mi = 0.0
    x_value_list = np.unique(x)
    y_value_list = np.unique(y)
    Px = np.array([ len(x[x==xval])/float(len(x)) for xval in x_value_list ]) #P(x)
    Py = np.array([ len(y[y==yval])/float(len(y)) for yval in y_value_list ]) #P(y)
    for i in range(len(x_value_list)):
        if Px[i] ==0.:
            continue
        sy = y[x == x_value_list[i]]
        if len(sy)== 0:
            continue
        pxy = np.array([len(sy[sy==yval])/float(len(y))  for yval in y_value_list]) #p(x,y)
        t = pxy[Py>0.]/Py[Py>0.] /Px[i] # log(P(x,y)/( P(x)*P(y))
        sum_mi += sum(pxy[t>0]*np.log2( t[t>0]) ) # sum ( P(x,y)* log(P(x,y)/( P(x)*P(y)) )
    return sum_mi



#
def compute_p_value(df, x, y, n_size = 90, perm = 500):
    actual_MI = compute_MI(df[x], df[y])


    deno = 1
    for i in range(perm):
        sample_df = df.copy()
        sample_df = sample_df.sample(n = n_size)
        # print(sample_df.shape)
        sample_MI = compute_MI(sample_df[x], sample_df[y])

        if sample_MI < actual_MI:
            # print(sample_MI, actual_MI)
            deno += 1
    return deno/(perm + 1)

def permutate_df_cols(df):

    pool = df.shape[1]

    pool = [i for i in range(pool)]

    col_combo = list(itertools.combinations(pool, 2))

    p_value_list = []
    counter = 1
    for x, y in col_combo:
        result = compute_p_value(df, x, y)
        p_value_list.append(result)
        print(f'Trial #{counter} done ({result} ({x},{y}))')
        counter += 1

    p_value_list.sort()

    return p_value_list

output_list = permutate_df_cols(df)
with open('sorted_p_values.json', 'w+') as outpuf_f:
    json.dump(output_list, outpuf_f)







