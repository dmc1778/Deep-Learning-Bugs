from datetime import date
import pandas as pd 
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv('test2.csv', sep=',')
    # df = data.sort_values('date', ascending=False)
    # df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    # df.to_csv('test2.csv', index=False)
    
    data['date'] = pd.DatetimeIndex(data['date']).year
    data.to_csv('test3.csv', index=False)
    # print(data)
    # ctdf = (data.reset_index()
    #       .groupby(['date','Type vis'], as_index=False)
    #       .count()
    #       .rename(columns={'index':'ct'}
    # ))
    # ctdf.to_csv('test3.csv', index=False)
    # fig, ax = plt.subplots()

    # key gives the group name (i.e. category), data gives the actual values
    # for key, data in ctdf.groupby('Library'):
    #     data.plot(x='date', y='ct', ax=ax, label=key)
    # plt.show()

if __name__ == "__main__":
    main()