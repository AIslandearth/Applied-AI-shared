import pandas as pd

dataset1 = "../Datasets/fingrid/ElectricityProductionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset2 = "../Datasets/fingrid/ElectricityConsumptionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset3 = "../Datasets/fingrid/SmallScaleElectricitySurplus_2026-02-17T0000_2026-03-17T0000.csv"

df = pd.read_csv(dataset3, sep=";")
print("")
print("Head: ")
print(df.head())
print("")
print("Info: ")
print(df.info())
print("")
print("Nulls: ")
print(df.isnull().sum())
print("")
print("Describe: ")
print(df.describe())
