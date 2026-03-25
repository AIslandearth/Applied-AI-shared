import pandas as pd
import matplotlib as plt
import numpy as np

class DatasetPreparation():
    def __init__(self, datasetIn, datasetOut, sep, column1, column2=None):
        self.datasetIn = datasetIn
        self.datasetOut = datasetOut
        self.columns = [column1, column2] if not column2 is None else [column1]
        self.sep = sep
        self.df = None
        self.dfOut = None
    def cleanup(self):
        self.df = pd.read_csv(self.datasetIn, sep=self.sep, usecols=self.columns)
        
        #self.df = self.df.sort_values(by=self.column).drop_duplicates(inplace=True).reset_index(drop=True)
        self.df = self.df.reset_index(drop=True)
        
        valuesAsNp = self.df[self.columns].values
        #print(valuesAsNp)
        
        # drop the remaining ones if less than four indexes remaining for calculating mean/avg
        n = (len(valuesAsNp) // 4) * 4
        
        if len(self.columns) == 1:
            # 15 min
            oneHour = np.round(valuesAsNp[:n].reshape(-1, 4).mean(axis=1), 1)
            self.dfOut = pd.DataFrame({'1 hour mean': oneHour})
        else:
            # already 1h
            oneHour = np.round(valuesAsNp, 1)
            self.dfOut = pd.DataFrame({'1 hour mean': oneHour}, columns=self.columns)
        
        print(oneHour)
        
        #sort_values(by=self.columns)
        
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