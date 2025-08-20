import csv
import matplotlib.pyplot as plt
from datetime import datetime



filename = './data/Marine_CSV_sample.csv'

#The csv module contains a next() function, which returns the next line
#in the file when passed the reader object
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    #print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    ## Get Air Temperature from this file
    dates, highs = [], []

    for row in reader:
        try:
            high = float(row[10])  # Air Temperature is in column 10
            highs.append(high)
            current_date = datetime.strptime(row[3], '%Y-%m-%dT%H:%M:%S')
            dates.append(current_date)
        except ValueError:
            print(f"Missing temperature data in row: {row[3]}")  # Show the time for missing data
        except IndexError:
            print(f"Row doesn't have enough columns: {row}")

    print(f"Found {len(highs)} temperature readings")
    print(f"First 10 temperatures: {highs[:10]}")

    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()

    #ax.plot(highs, c="red")
    # Format plot.
    plt.title("Daily high temperatures, July 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()