
import pandas as pd

def main():
    data = pd.read_csv('Tensorflow commits Review - Tensorflow raw.csv', sep=',')
    counts = data['Type'].value_counts().to_dict()
    df['Root Cause '] = df.groupby(['Date','Model']).transform('count')


if __name__ == "__main__":
    main()
