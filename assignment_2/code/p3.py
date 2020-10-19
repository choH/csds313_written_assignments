import random
import matplotlib.pyplot as plt
import statistics
import pandas as pd

M_size = 3000


E_M = []
E_MLE = []

def get_MLE(rockets, n):
    random.shuffle(rockets)
    E_M.append(len(rockets))

    x_list = random.choices(rockets, k = n)
    E_MLE.append(max(x_list))

mean_var = []
mvu_var = []

def get_vars(rockets, n):
    random.shuffle(rockets)
    x_list = random.choices(rockets, k = n)
    x_list.sort()

    mean_est = get_mean_est(x_list)
    MVU_est = get_MVU_est(x_list)
    # pop_mean = statistics.mean(rockets)
    sample_mean = statistics.mean(x_list)

    mean_var.append(calc_var(mean_est, sample_mean))
    mvu_var.append(calc_var(MVU_est, sample_mean))


def calc_var(est, mean):
    return (est - mean)**2

def get_mean_est(x_list):
    x_sum = sum(x_list)
    n = len(x_list)

    return 2 * x_sum - 1

def get_MVU_est(x_list):
    x_n = x_list[-1]
    n = len(x_list)

    return x_n * ((n+1)/n) - 1


trial_count = 20
counter = 1
for i in range(trial_count):
    rockets = [i for i in range(1, M_size)]
    n_size = random.randint(1, int(M_size/100))
    get_MLE(rockets, n_size)
    get_vars(rockets, n_size)

    print(f'{counter} done.')
    counter += 1




# (ii)
mvu_var_mean = statistics.mean(mvu_var)
mean_var_mean = statistics.mean(mean_var)
print(f'M_MVU average var: {mvu_var_mean}')
print(f'M_MEAN average var: {mean_var_mean}')
greater = 'M_MEAN' if mean_var_mean > mvu_var_mean else 'M_MVU'
print(f'{greater} is greater')

df = pd.DataFrame({'M_MEAN Var': mean_var,
                    'M_MVU Var': mvu_var})
df.reset_index().plot(x = 'index', y = ['M_MEAN Var', 'M_MVU Var'], kind='bar')
plt.show()



# (i)
# E_M_stacked = [i-j for i, j in zip(E_M, E_MLE)]
# r = [i for i in range(len(E_M_stacked))]
# plt.bar(r, E_MLE, color = 'b')
# plt.bar(r, E_M_stacked, bottom=E_MLE, color = 'r')
# plt.xlabel("Trials (M = 3000)")
# plt.show()
#
# print('done')



