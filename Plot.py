import numpy as np
import pandas as pd

data = pd.read_csv("K:\Projects\Dashboarding\seattle-crisis-data\crisis_data.csv")
#print(data['ReportedDate'])

data['ReportedDate'] = pd.to_datetime(data['ReportedDate'], format = "%d-%m-%Y")
#print(data['Reported Date'])

meets_by_month = data['ReportedDate'].groupby([data.ReportedDate.dt.year, data.ReportedDate.dt.month]).agg('count')
#print(meets_by_month)

meets_by_month = meets_by_month.to_frame()
#print(meets_by_month)

meets_by_month['Date'] = meets_by_month.index
#print(meets_by_month)

meets_by_month = meets_by_month.rename(columns = {meets_by_month.columns[0]:"crimes"})
#print(meets_by_month['Date'])

meets_by_month['Date'] = pd.to_datetime(meets_by_month['Date'], format = "(%Y, %m)")
#print(meets_by_month['Date'])

meets_by_month = meets_by_month.reset_index(drop = True)
#print(meets_by_month)

meets_by_month['month'] = meets_by_month.Date.dt.month
#print(meets_by_month)

"""disposition_issued = data['Disposition'].value_counts().to_frame()
#print(disposition_issued)

disposition_issued['disposition'] = disposition_issued.index
disposition_issued = disposition_issued.rename(columns = {disposition_issued.columns[0]:"crimes"})
print(disposition_issued)"""