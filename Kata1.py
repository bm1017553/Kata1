from pathlib import Path
import sys
import csv
import pandas as pd

file_path = Path("C:/Users/bmack/Desktop/Kata1/weatherdata.csv")

df = pd.read_fwf(file_path)

print(df.head())

# Check for command-line argument
if len(sys.argv) < 2:
    print("Usage: python Kata1.py <weather_file>")
    sys.exit(1)

input_path = Path(sys.argv[1])
output_path = Path("filtered_weather.csv")

with input_path.open("r", encoding="utf-8") as infile, \
     output_path.open("w", newline="", encoding="utf-8") as outfile:
    
    reader = infile.readlines()
    
    # Split header (fixed-width → split by whitespace)
    header = reader[0].split()
    
    # Create CSV writer
    writer = csv.writer(outfile)
    writer.writerow(["STATION", "DATE", "PRCP"])  # Output header
    
    # Find column positions
    prcp_index = header.index("PRCP")
    station_index = header.index("STATION")
    date_index = header.index("DATE")
    
    for line in reader[1:]:
        parts = line.split()
        
        if len(parts) <= prcp_index:
            continue
        
        try:
            prcp_value = float(parts[prcp_index])
        except ValueError:
            continue
        
        if prcp_value > 15:
            writer.writerow([
                parts[station_index],
                parts[date_index],
                prcp_value
            ])

print(f"Filtered data written to {output_path.resolve()}")