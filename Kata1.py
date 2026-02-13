from pathlib import Path
import sys
import pandas as pd

file_path = Path("C:/Users/bmack/Desktop/Kata1/weatherdata.csv")

df = pd.read_fwf(file_path)

print(df.head())

if len(sys.argv) < 2:
    print("Usage: python Kata1.py <weather_file>")
    sys.exit(1)

file_path = Path(sys.argv[1])

with file_path.open("r", encoding="utf-8") as file:
    header = file.readline().strip().split()
    
    # Find column indexes dynamically
    prcp_index = header.index("PRCP")
    station_index = header.index("STATION")
    date_index = header.index("DATE")
    
    for line in file:
        parts = line.split()
        
        # Skip malformed lines
        if len(parts) <= prcp_index:
            continue
        
        try:
            prcp_value = float(parts[prcp_index])
        except ValueError:
            continue
        
        if prcp_value > 15:
            print(parts[station_index], parts[date_index], prcp_value)