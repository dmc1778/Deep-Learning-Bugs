from numpy.random.mtrand import f
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt



def main():
    mean_history = []
    data = pd.read_csv('Tensorflow commits Review - fixing scale corr.csv', sep=',')
    #counts = data['Type'].value_counts().to_dict()
    # df_heatmap = data.pivot_table(values='Root cause High level',index='Root cause High level',columns='Type vis',aggfunc=np.mean)
    # sns.heatmap(df_heatmap,annot=True)
    # plt.show()

    tensorflow = pd.Series(np.random.choice(data['Tensorflow'], replace=False, size=30))
    PyTorch = pd.Series(np.random.choice(data['PyTorch'], replace=False, size=30))
    Pandas = pd.Series(np.random.choice(data['Pandas'], replace=False, size=30))
    Numpy = pd.Series(np.random.choice(data['Numpy'], replace=False, size=30))
    # tensorflow = data['Tensorflow'].sample(n=30, random_state=2)
    # PyTorch = data['PyTorch'].sample(n=30, random_state=2)
    # Pandas = data['Pandas'].sample(n=30, random_state=2)
    # Numpy = data['Numpy'].sample(n=30, random_state=2)

    a = ['Tensorflow', 'PyTorch', 'Sklearn', 'Pandas', 'Numpy']
    b = ['Tensorflow', 'PyTorch', 'Sklearn', 'Pandas', 'Numpy']

    new_df = { 'Tensorflow': tensorflow, 'PyTorch': PyTorch \
        ,  'Pandas': Pandas, 'Numpy': Numpy, "Sklearn": data['Sklearn'] }

    data = pd.DataFrame(new_df)

    # df2 = pd.DataFrame(np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]\
    #     ,[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),columns=['Tensorflow', 'PyTorch', 'Keras', 'Sklearn', 'Pandas', 'Numpy']\
    #         ,index=['Tensorflow', 'PyTorch', 'Keras', 'Sklearn', 'Pandas', 'Numpy'])
    
    corr = data.apply(lambda x : pd.factorize(x)[0]).corr(method='pearson', min_periods=30)
    mean_history.append(np.mean(corr.values))
    sns.heatmap(corr, cmap="Blues", annot=True)
    plt.show()
    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         if i != j:
    #             CrosstabResult=pd.crosstab(index=data[a[i]],columns=data[a[j]])
    #             ChiSqResult = chi2_contingency(CrosstabResult)
    #             df2.iloc[i,j] = df2.corr
    #         else:
    #             df2.iloc[i,j] = 0
    #             # print(a[i],' and ',a[j])
    #             # print('The P-Value of the ChiSq Test is:', ChiSqResult[1])

    # print(df2)

if __name__ == "__main__":
    main()
