import numpy as np
import pandas as pd

data = pd.read_csv("K:\Projects\Dashboarding\seattle-crisis-data\crisis_data.csv")
#print(data['ReportedDate'])

data['ReportedDate'] = pd.to_datetime(data['ReportedDate'], format = "%d-%m-%Y")
#print(data['Reported Date'])

crimes_by_month = data['ReportedDate'].groupby([data.ReportedDate.dt.year, data.ReportedDate.dt.month]).agg('count')
#print()

crimes_by_month = crimes_by_month.to_frame()
#print(crimes_by_month)

crimes_by_month['Date'] = crimes_by_month.index
#print(crimes_by_month)

crimes_by_month = crimes_by_month.rename(columns = {crimes_by_month.columns[0]:"crimes"})
#print(crimes_by_month['Date'])

crimes_by_month['Date'] = pd.to_datetime(crimes_by_month['Date'], format = "(%Y, %m)")
#print(crimes_by_month['Date'])

crimes_by_month = crimes_by_month.reset_index(drop = True)
#print(crimes_by_month)

crimes_by_month['month'] = crimes_by_month.Date.dt.month
#print(crimes_by_month)

"""disposition_issued = data['Disposition'].value_counts().to_frame()
#print(disposition_issued)

disposition_issued['disposition'] = disposition_issued.index
disposition_issued = disposition_issued.rename(columns = {disposition_issued.columns[0]:"crimes"})
print(disposition_issued)"""