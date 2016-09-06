#PDSI_Download.py

import numpy as np
import datetime
import wget
import re

def years(start, end, flag):
    """Download data from a specified year range

    Keyword Args:
    start -- First year in range of years
    end -- Final year in range of years
    flag -- Flag to determine whether user wants to DL data or compute PDSI on data
    """
    def month_check(year):
        """Compute the current month

        Keyword Args:
        year -- Year to check whether or not user wants data from the current year
        """
        date = str(datetime.datetime.now())
        date_arr = re.split("-", date)
        current_year = int(date_arr[0])
        current_month = date_arr[1]
        if current_year == year:
            if current_month[0] == 0:
                return int(current_month[-1])
            else:
                return int(current_month)
        else:
            return 0

    def download_data(start, end):
        """Downloads PDSI data in netCDF format in a range of years

        Keyword Args:
        start -- First year in range of years
        end -- Final year in range of years
        """
        year = start
        year_range = (end - start) + 1
        number_of_months = year_range * 12
        current_month = month_check(end)

        #If user is trying to get data from current year, factor our months that have yet to occur + 1
        if current_month != 0:
            number_of_months -= (13 - current_month)

        for i in range(0, number_of_months):
            month = (i % 12) + 1
            if i > 0 and i % 12 == 0:
                year += 1
            print("Month: %i, Year: %i" % (month, year))
            URL = "http://www.wrcc.dri.edu/wwdt/data/PRISM/spi1/spi1_" + str(year) + "_" + str(month) + "_PRISM.nc"
            wget.download(URL)


    download_data(start, end)

def year(year, flag):
    """Download data from a specified year

        Keyword Args:
        year -- Year user wants data from
        flag -- Flag to determine whether user wants to DL data or compute PDSI on data
        """
    def month_check(year):
        """Compute the current month

        Keyword Args:
        year -- Year to check whether or not user wants data from the current year
        """
        date = str(datetime.datetime.now())
        date_arr = re.split("-", date)
        current_year = int(date_arr[0])
        current_month = date_arr[1]
        if current_year == year:
            if current_month[0] == 0:
                return int(current_month[-1]) - 1
            else:
                return int(current_month) - 1
        else:
            return 12


    def download_data(year):
        """Downloads PDSI data in netCDF format from a specified year

        Keyword Args:
        year -- Year user wants data from
        """
        for i in range(0, month_check(year)):
            month = (i % 12) + 1
            print("Month: %i, Year: %i" % (month, year))
            URL = "http://www.wrcc.dri.edu/wwdt/data/PRISM/spi1/spi1_" + str(year) + "_" + str(month) + "_PRISM.nc"
            wget.download(URL)

    download_data(year)

def months(month_range, start, end, flag):
    """Download data from a specified year range

    Keyword Args:
    month_range -- Array of months (numeric, i.e. January = 1) user wants data from
    start -- First year in range of years
    end -- Final year in range of years
    flag -- Flag to determine whether user wants to DL data or compute PDSI on data
    """
    def download_data(month_range, start, end):
        """Downloads PDSI data in netCDF format from specified months and years

        Keyword Args:
        month_range -- Array of months (numeric, i.e. January = 1) user wants data from
        start -- First year in range of years
        end -- Final year in range of years
        """
        year = start
        years_in_range = (end - start) + 1
        months_in_range = len(month_range)
        number_of_months = months_in_range * years_in_range

        for i in range(0, number_of_months):
            month = month_range[i % months_in_range]
            if i > 0 and i % months_in_range == 0:
                year += 1
            print("Month: %i, Year: %i" % (month, year))
            URL = "http://www.wrcc.dri.edu/wwdt/data/PRISM/spi1/spi1_" + str(year) + "_" + str(month) + "_PRISM.nc"
            wget.download(URL)

    download_data(month_range, start, end)

#years(2010, 2011, "z")
#year(2015, "z")
months([1, 2, 5], 2010, 2011, "z")





