from scipy.stats import norm,uniform 
import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def calc_percentile():
    print(norm.ppf(0.25,2,5))
    print(norm.ppf(0.75,2,5))

def sample_n():
    np.random.seed(1)
    sample = norm.rvs(loc=2, scale=5, size=10000)
    x = np.arange(35)
    df = pd.DataFrame(sample)
    # boxplot:
    # df.boxplot() 
    # histogram: 
    n, bins, _ = plt.hist(sample,bins=25,density=False,alpha=0.6,color='g')
    mid = 0.5*(bins[1:] + bins[:-1])
    plt.errorbar(mid, n, yerr=np.sqrt(n), fmt='none')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, 2, 5)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit Results: mu = %.2f,  std = %.2f" % (2, 5)
    plt.title(title)
    plt.show()

def sample_u1(): 
    np.random.seed(1)
    sample = uniform.rvs(loc=2-5*math.sqrt(3), scale=10*math.sqrt(3), size=10000)
    n, bins, _ = plt.hist(sample,bins=25,density=False,alpha=0.6,color='b')
    mid = 0.5*(bins[1:] + bins[:-1])
    plt.errorbar(mid, n, yerr=np.sqrt(n), fmt='none')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 50)
    p = uniform.pdf(x, 2-5*math.sqrt(3), 10*math.sqrt(3))
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit Results: a = %.2f,  b = %.2f" % (2-5*math.sqrt(3), 2+5*math.sqrt(3))
    plt.title(title)
    # df = pd.DataFrame(sample)
    # df.boxplot()
    plt.show()

def sample_u2(): 
    np.random.seed(1)
    sample = uniform.rvs(loc=-1.3724, scale=6.7448, size=10000)
    n, bins, _ = plt.hist(sample,bins=25,density=False,alpha=0.6,color='y')
    mid = 0.5*(bins[1:] + bins[:-1])
    plt.errorbar(mid, n, yerr=np.sqrt(n), fmt='none')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 50)
    p = uniform.pdf(x, -1.3723, 6.7448)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit Results: a = %.2f,  b = %.2f" % (-1.3724, 5.3724)
    plt.title(title)
    # df = pd.DataFrame(sample)
    # df.boxplot()
    plt.show()

sample_u2()