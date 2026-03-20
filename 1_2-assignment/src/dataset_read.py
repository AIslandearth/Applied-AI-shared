import pandas as pd
import matplotlib as plt
from dataset_cleanup import DatasetPreparation

dataset1 = "1_2-assignment/Datasets/fingrid/ElectricityProductionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset2 = "1_2-assignment/Datasets/fingrid/ElectricityConsumptionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset3 = "1_2-assignment/Datasets/fingrid/SmallScaleElectricitySurplus_2026-02-17T0000_2026-03-17T0000.csv"

# df = pd.read_csv(dataset3, sep=";")
# print("")
# print("Head: ")
# print(df.head())
# print("")
# print("Info: ")
# print(df.info())
# print("")
# print("Nulls: ")
# print(df.isnull().sum())
# print("")
# print("Describe: ")
# print(df.describe())

dp = DatasetPreparation(dataset1, "modifiedDataSet.csv", 'Electricity production in Finland', sep=';')
dp.cleanup()
