import argparse
import csv
from pathlib import Path
from datetime import datetime
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Filter weather records where PRCP > 15"
    )

    parser.add_argument("input_file", help="Path to input weather file")
    parser.add_argument("output_file", help="Path to output CSV file")
    parser.add_argument(
        "--log",
        default="weather_processing.log",
        help="Path to log file (default: weather_processing.log)"
    )

    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)
    log_path = Path(args.log)

    if not input_path.exists():
        print(f"Error: Input file '{input_path}' does not exist.")
        sys.exit(1)

    records_read = 0
    records_written = 0

    try:
        with input_path.open("r", encoding="utf-8") as infile, \
             output_path.open("w", newline="", encoding="utf-8") as outfile:

            writer = csv.writer(outfile)

            header = infile.readline().split()
            writer.writerow(["STATION", "DATE", "PRCP"])

            prcp_index = header.index("PRCP")
            station_index = header.index("STATION")
            date_index = header.index("DATE")

            for line in infile:
                records_read += 1
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
                    records_written += 1

        print(f"Filtered data written to {output_path.resolve()}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    # ---------------------------
    # Logging (Append Mode)
    # ---------------------------
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with log_path.open("a", encoding="utf-8") as logfile:
        logfile.write(
            f"{timestamp} | Input: {input_path} | "
            f"Read: {records_read} | "
            f"Written: {records_written}\n"
        )


if __name__ == "__main__":
    main()