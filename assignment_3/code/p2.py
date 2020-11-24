import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


df_2a = pd.read_csv('assignment_3/data/p2a.csv', header=None)
df_2b = pd.read_csv('assignment_3/data/p2b.csv', header=None)
df_2c = pd.read_csv('assignment_3/data/p2c.csv', header=None)


print(f'p2a.csv Corr: {stats.pearsonr(df_2a[0], df_2a[1])[0]}; P-value: {stats.pearsonr(df_2a[0], df_2a[1])[1]}')
print(f'p2b.csv Corr: {stats.pearsonr(df_2b[0], df_2b[1])[0]}; P-value: {stats.pearsonr(df_2b[0], df_2b[1])[1]}')
print(f'p2c.csv Corr: {stats.pearsonr(df_2c[0], df_2c[1])[0]}; P-value: {stats.pearsonr(df_2c[0], df_2c[1])[1]}')

def pearsonr_ci(x,y,alpha=0.05):
    '''
    calculate Pearson correlation along with the confidence interval using scipy and numpy
    Parameters
    ----------
    x, y : iterable object such as a list or np.array
      Input for correlation calculation
    alpha : float
      Significance level. 0.05 by default
    Returns
    -------
    r : float
      Pearson's correlation coefficient
    pval : float
      The corresponding p value
    lo, hi : float
      The lower and upper bound of confidence intervals
    '''
    r, p = stats.pearsonr(x,y)
    r_z = np.arctanh(r)
    se = 1/np.sqrt(x.size-3)
    z = stats.norm.ppf(1-alpha/2)
    lo_z, hi_z = r_z-z*se, r_z+z*se
    lo, hi = np.tanh((lo_z, hi_z))
    return r, p, lo, hi

print(pearsonr_ci(df_2a[0], df_2a[1]))
print(pearsonr_ci(df_2b[0], df_2b[1]))
print(pearsonr_ci(df_2c[0], df_2c[1]))



# plt_2a = df_2a.plot.scatter(x = 0, y = 1)
# plt_2a.set_aspect('equal')
# plt_2a.set_adjustable("datalim")
# plt.title('p2a.csv')

# plt_2b = df_2b.plot.scatter(x = 0, y = 1)
# plt_2b.set_aspect('equal')
# plt_2b.set_adjustable("datalim")
# plt.title('p2b.csv')


# plt_2c = df_2c.plot.scatter(x = 0, y = 1)
# plt_2c.set_aspect('equal')
# plt_2c.set_adjustable("datalim")
# plt.title('p2c.csv')
#
#
# plt.show()
