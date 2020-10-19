from scipy.stats import norm,uniform 
import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import powerlaw
import pylab

def unif():
    # df = pd.read_csv("airport_routes.csv") 
    # print("a = ", df.min(), ", b = ", df.max())
    # df = pd.read_csv("movie_votes.csv") 
    # print("a = ", df.min(), ", b = ", df.max())


    # np.random.seed(1)
    # sample = uniform.rvs(loc=1, scale=914, size=10000)
    # plt.hist(sample,bins=25,density=False,alpha=0.6,color='b')
    # xmin, xmax = plt.xlim()
    # x = np.linspace(xmin, xmax, 50)
    # p = uniform.pdf(x, 1, 915)
    # plt.plot(x, p, 'k', linewidth=2)
    # title = "Fit Results: a = %.2f,  b = %.2f" % (1, 915)
    # plt.title(title)

    sample = uniform.rvs(loc=1.9, scale=6.6, size=10000)
    plt.hist(sample,bins=25,density=False,alpha=0.6,color='b')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 50)
    p = uniform.pdf(x, 1, 915)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit Results: a = %.2f,  b = %.2f" % (1.9, 8.5)
    plt.title(title)
    plt.show()

def normal(): 
    # df = pd.read_csv("airport_routes.csv")
    # mean = df.mean(axis=0)
    # std = df.std(axis=0)

    df = pd.read_csv("movie_votes.csv") 
    mean = df.mean(axis=0)
    std = df.std(axis=0)
    # print(mean, std)

    np.random.seed(1)
    sample = norm.rvs(loc=mean, scale=std, size=10000)
    plt.hist(sample,bins=25,density=False,alpha=0.6,color='g')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit Results: mu = %.2f,  std = %.2f" % (mean, std)
    plt.title(title)
    plt.show()

def power():
    df = pd.read_csv("movie_votes.csv")
    array = df['AverageVote'].to_numpy()
    sum = 0
    for i in array: 
        sum += np.log(i/1.9)
    a = 1 + 4392 * sum**(-1)
    samples = 10000
    s = np.random.power(a, 10000)
    count, bins, ignored = plt.hist(s, bins=30)
    x = np.linspace(0, 1, 100)
    y = a*x**(a-1.)
    normed_y = samples*np.diff(bins)[0]*y
    plt.plot(x, normed_y)
    plt.show()

def exponential():
    df = pd.read_csv("airport_routes.csv")
    l = 1/df.mean()
    sample = np.random.exponential(scale=1/l,size=10000)
    sample.sort()
    count, bins, ignored = plt.hist(sample, bins=30,density=False)
    x = np.linspace(0, 1, 10000)
    plt.plot(x, sample)
    plt.show()

def data():
    df = pd.read_csv("movie_votes.csv")
    array = df['AverageVote']
    count, bins, ignored = plt.hist(array, bins=30,density=False, color='r',alpha=0.7)
    x = np.linspace(0, 1, 4392)
    plt.plot(x, array)
    plt.show()

data()