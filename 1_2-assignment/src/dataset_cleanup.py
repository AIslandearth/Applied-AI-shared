import pandas as pd
import matplotlib as plt
import numpy as np

class DatasetPreparation():
    def __init__(self, datasetIn, datasetOut, sep, timestamp, value, type=None):
        self.datasetIn = datasetIn
        self.datasetOut = datasetOut
        self.timestamp = timestamp
        self.value = value
        self.type = type
        self.sep = sep
        self.df = None
        self.dfOut = None
    def cleanup(self):
        if self.type is None:
            usecols = [self.timestamp, self.value]
        else:
            usecols = [self.timestamp, self.value, self.type]
        
        self.df = pd.read_csv(self.datasetIn, sep=self.sep, usecols=usecols)
        
        self.df[self.timestamp] = pd.to_datetime(self.df[self.timestamp])
        self.df = self.df.sort_values(self.timestamp)
        
        if self.type is not None:
            dfPivot = self.df.pivot_table(index=self.timestamp, columns=self.type, values=self.value, aggfunc='mean')
        else:
            dfPivot = self.df.set_index(self.timestamp)
        
        dfHour = dfPivot.resample('1h').mean().round(1)
        
        self.dfOut = dfHour.reset_index()
        print(self.dfOut.head())
        
        self.dfOut.to_csv(self.datasetOut, index=False, sep=self.sep)
        
        return self