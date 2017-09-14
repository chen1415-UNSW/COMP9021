# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx--xxxx, and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the second year can be anterior to the first year.
# - The month is a two digit number.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import re
import statistics

filename = 'monthly.csv'
if not os.path.exists(filename):
    print('There is no file named {} in the working directory, giving up...'.format(filename))
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
range_for_the_years = input('Enter a range for the years in the form XXXX--XXXX: ')
month = input('Enter a month in the form of a 2-digit number: ')
average = 0
years_above_average = []

range_for_the_years.split()
if(int(range_for_the_years[0:4])>=int(range_for_the_years[6:10])):
    year_up=int(range_for_the_years[0:4])
    year_down=int(range_for_the_years[6:10])
else:
    year_down=int(range_for_the_years[0:4])
    year_up=int(range_for_the_years[6:10])
#print(year_up)
#print(year_down)
average_GCAG = 0
average_GISTEMP = 0

with open(filename) as csvfile:
    L_count_GCAG=[]
    L_count_GISTEMP=[]
    year_GCAG=[]
    year_GISTEMP=[]
    for line in csvfile:
        #print('1', line)
        data=''
        data=line
        if(data.startswith('Source')==True):
            #print('1',data)
            continue
        if(data[0:4]==source):
            #print(data) #this is GCAG
            data=data.split(',')
            #print(data)
            #print(int(data[1][0:4]))
            #print(int(data[1][5:7]))
            if(int(data[1][0:4]) >= year_down and int(data[1][0:4])<=year_up and int(data[1][5:7])==int(month)):
                L_count_GCAG.append(float(data[2]))
                year_GCAG.append([int(data[1][0:4]),float(data[2])])
                #print(year_GCAG)
        if(data[0:7]==source):
            #print(data)
            data=data.split(',')
            #print(data)
            if(int(data[1][0:4]) >= year_down and int(data[1][0:4])<=year_up and int(data[1][5:7])==int(month)):
                L_count_GISTEMP.append(float(data[2]))
                year_GISTEMP.append([int(data[1][0:4]),float(data[2])])
                #print(data[2])
                #print(L_count_GISTEMP)
    if(source=='GCAG'):
        #print(L_count_GCAG)
        average_GCAG=statistics.mean(L_count_GCAG)
        #print(average_GCAG)
        average=average_GCAG
        for i in year_GCAG:
            if(i[1]>average):
                years_above_average.append(i[0])
                years_above_average=sorted(years_above_average)               
    else:
        #print(L_count_GISTEMP)
        average_GISTEMP=statistics.mean(L_count_GISTEMP)
        average=average_GISTEMP
        for i in year_GISTEMP:
            if(i[1]>average):
                years_above_average.append(i[0])
                years_above_average=sorted(years_above_average) 
    

                
    
 
print('The average anomaly for this month of those years is: {:.2f}.'.format(average))
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)
