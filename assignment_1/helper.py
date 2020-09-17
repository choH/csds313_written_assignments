import pandas as pd
from os.path import expanduser as ospath
import matplotlib.pyplot as plt

df = pd.read_excel('./assignment_1/covid_data.xlsx')

def p1():
    print(df.shape[0])

def p2():
    print(df['countriesAndTerritories'].nunique())
    print(df.dateRep.min(), df.dateRep.max())

def p3_1():
    countries = []
    populations = []
    i = 0
    for country in df['countriesAndTerritories']:
        if country not in countries:
            countries.append(country)
            pop = df.at[df['countriesAndTerritories'].eq(country).idxmax(),'popData2019'].astype('float')
            populations.append(pop)
            i += 1
    df2 = pd.DataFrame({'country': countries,
                       'population': populations})
    mean = df2['population'].mean()
    print(mean)
    variance = df2['population'].var()
    print(variance)

def p3_2():
    i = 0
    countries = []
    populations = []
    for country in df['countriesAndTerritories']:
        if country not in countries:
            countries.append(country)
            pop = df.at[df['countriesAndTerritories'].eq(country).idxmax(),'popData2019'].astype('float')
            populations.append(pop)
            i += 1
    df2 = pd.DataFrame({'country': countries, 'population': populations})
    mean = df2['population'].mean()
    print(mean)
    std = df2['population'].std()
    print(std)
    df2['population'].hist(range = [0,200000000])
    plt.show()


def p4():
    mask = (df['dateRep'] == '2020-05-04')
    df2 = df.loc[mask]
    print(df2['cases'].median())
    q1 = df2['cases'].quantile(0.25)
    q3 = df2['cases'].quantile(0.75)
    print(q3 - q1)
    df2['cases'].hist(range = [0,10000])
    plt.show()

def p5():
    # mask = (df['dateRep'] >= '2020-06-01') & (df['dateRep'] <= '2020-07-01')
    # df2 = df.loc[mask]
    # df2 = df2[['countriesAndTerritories','cases']]
    # df2 = df2.sort_values('cases',ascending=False)
    mask = (df['dateRep'] >= '2020-06-01') & (df['dateRep'] <= '2020-07-01')
    df2 = df.loc[mask]
    df2 = df2[['countriesAndTerritories','cases']]
    df2 = df2.groupby(['countriesAndTerritories']).sum()
    df2 = df2.sort_values('cases',ascending=False)
    print(df2.head())

def p6():
    mask = (df['dateRep'] >= '2020-06-01') & (df['dateRep'] <= '2020-07-01')
    df2 = df.loc[mask]
    df2 = df2[['countriesAndTerritories','cases']]
    df2 = df2.groupby(['countriesAndTerritories']).sum()
    df2['cases'] = df2['cases']/31
    df2 = df2.sort_values('cases',ascending=False)
    print(df2)

def p7():
    mask = (df['dateRep'] >= '2020-06-01') & (df['dateRep'] <= '2020-07-01')
    df2 = df.loc[mask]
    df2 = df2[['countriesAndTerritories','cases','popData2019']]
    df2 = df2.groupby(['countriesAndTerritories','popData2019'],as_index=False).sum()
    df2["result"] = ""
    df2['result'] = df2['cases']/df2['popData2019']*10000
    df2 = df2.sort_values('result',ascending=False)
    print(df2)

def p8():
    df2 = df[['dateRep','countriesAndTerritories','cases','deaths']]
    df2 = df2.groupby(['dateRep']).sum().sort_values('cases',ascending=False)
    #print(df2)
    df2 = df2.sort_values('deaths',ascending=False)
    print(df2)

def p9():
    df_holder = (df['dateRep'] >= '2020-06-01') & (df['dateRep'] <= '2020-08-01')
    df_holder = df.loc[df_holder]
    df_holder = df_holder[['dateRep','countriesAndTerritories','cases','deaths']]
    df_us_case = df_holder.loc[df['countriesAndTerritories'] == 'United_States_of_America']

    df_us_case.plot(x = 'dateRep', y = ['deaths', 'cases'])
    plt.show()
    # df_us_case.plot(x = 'dateRep', y = 'deaths')
    # plt.show()


def p10():
    # df_holder = (df['dateRep'] >= '2020-04-01') & (df['dateRep'] <= '2020-4-30')
    # df_holder = df.loc[df_holder]
    # df_holder = df_holder[['dateRep','countriesAndTerritories','cases','popData2019', 'continentExp']]
    # sa_major_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Uruguay', 'Venezuela']
    # df_sa_case = df_holder.loc[df['countriesAndTerritories'].isin(sa_major_countries)]
    # df_sa_case = df_sa_case.groupby(['countriesAndTerritories','popData2019'], as_index = False )['cases'].sum()
    #
    # df_sa_case['case_per_pop'] = df_sa_case['cases'] / df_sa_case['popData2019'] * 100
    # df_sa_case.sort_values(by = ['case_per_pop'], ascending = False)
    # print(df_sa_case.head())


    df_holder = (df['dateRep'] >= '2020-04-01') & (df['dateRep'] <= '2020-4-30')
    df_holder = df.loc[df_holder]
    df_holder = df_holder[['dateRep','countriesAndTerritories','cases','popData2019', 'continentExp']]
    df_case = df_holder.groupby(['countriesAndTerritories','popData2019'], as_index = False )['cases'].sum()

    df_case['case_per_pop'] = df_case['cases'] / df_case['popData2019'] * 100
    df_case = df_case.sort_values(by = ['case_per_pop'], ascending = False)
    print(df_case.head())

def p11():
    df_holder = df[['dateRep', 'countriesAndTerritories','cases','popData2019', 'continentExp']]
    df_continent_case = df_holder.groupby(['continentExp'], as_index = False )['cases'].sum()

    df_country_pop = df_holder.groupby(['countriesAndTerritories', 'continentExp'], as_index = False )['popData2019'].first()
    df_continent_pop = df_country_pop.groupby(['continentExp'], as_index = False)['popData2019'].sum()
    df_continent = pd.merge(df_continent_case, df_continent_pop, on = 'continentExp')
    df_continent['case_per_m'] = df_continent['cases'] / df_continent['popData2019'] * 1000000

    df_continent = df_continent.sort_values(by = ['case_per_m'], ascending = False)
    df_continent_case = df_continent_case.sort_values(by = ['cases'], ascending = False)
    print(df_continent_case.head())
    print(df_continent.head())


p10()