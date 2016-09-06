# PDSI_Download.py

from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import wget
import os

class DateRange():
    def __init__(self, start_year, end_year, month_range):
        self.start_year = start_year
        self.end_year = end_year
        self.month_range = month_range

def PDSI(date_range, flag):
    def get_date_range(date_range):
        #Specify months to download
        if date_range.month_range == None:
            months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        else:
            months = date_range.month_range

        #Specify years to download
        years = []
        if date_range.start_year == date_range.end_year:
            years.append(date_range.end_year)
        else:
            for year in range(date_range.start_year, date_range.end_year + 1):
                years.append(year)

        #Return list of months and list of years
        return months, years

    def download(date_range):
        months, years = get_date_range(date_range)
        num_months = len(years) * len(months)
        year_iter = -1

        new_dir = str(os.getcwd()) + "/PDSI_Data"
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            os.chdir(new_dir)
        else:
            os.chdir(new_dir)

        for i in range(0, num_months):
            month = months[i % len(months)]

            if i % len(months) == 0:
                year_iter += 1
                year = years[year_iter]

            print("Month: %i, Year: %i" % (month, year))
            URL = "http://www.wrcc.dri.edu/wwdt/data/PRISM/spi1/spi1_" + str(year) + "_" + str(month) + "_PRISM.nc"
            #wget.download(URL)

    def visualize():
        cwd = str(os.getcwd())
        os.chdir(cwd + "/PDSI_Data")
        files = os.listdir()
        for i in range(0, len(files)):
            file = Dataset(files[i], "r")
            print(file)
            print(file.variables["longitude"])
            print(file.variables["latitude"])
            print(file.variables["day"])
            print(file.variables["data"])

    #download(date_range)
    visualize()


dates = DateRange(2012, 2012, [1])
PDSI(dates, "x")