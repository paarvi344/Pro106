import csv
import numpy as np

def setup():
    data_path = "marksVsattendance.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

def getDataSource(data_path):
    MarksOfStudent = []
    Attendance = []
    with open (data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader :
            MarksOfStudent.append(float(row['Marks In Percentage']))
            Attendance.append(float(row['Days Present']))

    return {"x" : MarksOfStudent, "y": Attendance}