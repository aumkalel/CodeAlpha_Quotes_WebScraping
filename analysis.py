import pandas as pd

df = pd.read_csv("quotes_dataset.csv")

print("Total Quotes:", len(df))

print("\nTop Authors:")
print(df["Author"].value_counts().head())