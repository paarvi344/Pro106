import csv
import numpy as np

def setup():
    data_path = "CupsOfCoffeeVSHours.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

def getDataSource(data_path):
    CupsOfCoffee = []
    HoursOfSleep = []
    with open (data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader :
            CupsOfCoffee.append(float(row['Coffee in ml']))
            HoursOfSleep.append(float(row['sleep in hours']))

    return {"x" : CupsOfCoffee, "y": HoursOfSleep}

        