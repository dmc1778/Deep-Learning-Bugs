
from os import sep
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def load_csv():
    file_path = 'D:\\vsprojects\\deepLearningbugs\\Tensorflow commits Review - without Keras.csv'
    return pd.read_clipboard(file_path, sep=',')

def plot(df):
    df.pivot_table(index='Library', columns='Type vis', values='Type vis')
    ax = df.T.plot(kind='bar', ylabel='Murder Rate')
    plt.plot()

def main():
    data = load_csv()
    plot(data)


if __name__ == '__main__':
    main()