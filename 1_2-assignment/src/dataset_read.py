import pandas as pd

dataset1 = "./Datasets/fingrid/ElectricityProductionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset2 = "./Datasets/fingrid/ElectricityConsumptionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset3 = "./Datasets/fingrid/SmallScaleElectricitySurplus_2026-02-17T0000_2026-03-17T0000.csv"

df = pd.read_csv(dataset1)
df.head()
df.info()
df.describe()

print("Hello")
