from pathlib import Path
import pandas as pd

file_path = Path("C:/Users/bmack/Desktop/Kata1/weatherdata.csv")

df = pd.read_fwf(file_path)

print(df.head())