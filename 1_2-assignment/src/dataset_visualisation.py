import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function for visualization for calling from other blocks
def datasetVisualization(dataset):
    
    # Dataset reading
    df = pd.read_csv(dataset, sep=";", quotechar='"')

    print("\n=== HEAD ===")
    print(df.head())

    print("\n=== INFO ===")
    print(df.info())

    print("\n=== DESCRIBE ===")
    print(df.describe(include="all"))

    print("\n=== MISSING VALUES ===")
    print(df.isnull().sum())

    print("\n=== UNIQUE VALUES ===")
    print(df.nunique())
    
    # Select numeric column from dataset
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    
    if len(numeric_cols) == 0:
        print("No numeric columns!")
        return
    
    col = numeric_cols[0]
    print(f"Using column: {col}")

    # Visualizations
    if col in df.columns:
        sns.histplot(df[col])
        plt.title(f"Histogram: {col}")
        plt.show()

        sns.boxplot(x=df[col])
        plt.title(f"Boxplot: {col}")
        plt.show()
    else:
        print(f"⚠ Saraketta '{col}' ei löydy datasetistä!")

# Dataset-paths
dataset1 = "../Datasets/fingrid/ElectricityProductionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset2 = "../Datasets/fingrid/ElectricityConsumptionFinland_2026-02-17T0000_2026-03-17T0000.csv"
dataset3 = "../Datasets/fingrid/SmallScaleElectricitySurplus_2026-02-17T0000_2026-03-17T0000.csv"

# Function for testing
datasetVisualization(dataset3)