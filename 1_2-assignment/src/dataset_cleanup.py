import pandas as pd
import matplotlib as plt
import numpy as np

class DatasetPreparation():
    def __init__(self, datasetIn, datasetOut, column, sep):
        self.datasetIn = datasetIn
        self.datasetOut = datasetOut
        self.column = column
        self.sep = sep
        self.df = None
        self.dfOut = None
    def cleanup(self):
        self.df = pd.read_csv(self.datasetIn, sep=self.sep, usecols=[self.column])
        
        self.df = self.df.sort_values(by=self.column).reset_index(drop=True)
        
        valuesAsNp = self.df[self.column].values
        print(valuesAsNp)
        
        quadGroups = valuesAsNp.reshape(-1, 4)
        print(quadGroups)
        
        meansAsNp = np.round(quadGroups.mean(axis=1), 1)
        print(meansAsNp)
        
        self.dfOut = pd.DataFrame({'1H mean': meansAsNp})
        self.dfOut.to_csv(self.datasetOut, index=False, sep=self.sep)
        #np.savetxt(self.datasetOut, meansAsNp, delimiter=self.sep, header='1H mean', comments='')
        
        # print("\n")
        # print(self.df.dtypes)
        # print("\n")
        # print(self.df.isnull().sum())
        # print("\n")
        # print(self.df.describe())
        # np.drop_duplicates(inplace=True)
        
        return self