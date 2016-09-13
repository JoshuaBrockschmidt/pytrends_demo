#!/usr/bin/env python3

from datetime import datetime
from getpass import getpass
from matplotlib import pyplot
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from pytrends.request import TrendReq
from pprint import PrettyPrinter

# Get trend data
username = input('Enter your Gmail address: ')
password = getpass('Enter your password: ')
trendGet = TrendReq(username, password, custom_useragent='Python pytrends demo')
query = input('Enter keywords to search: ')
payload = {'q' : query.replace(',', '')}
trend = trendGet.trend(payload)

# Organize trend data
x = []
y = []
rows = trend['table']['rows']
cols = trend['table']['cols']
for _, v in enumerate(rows):
    date = datetime.strptime(v['c'][0]['v'], '%Y-%m-%d')
    x.append(date)
    y.append(v['c'][1]['v'])

# Graph trend data
years = YearLocator()
months = MonthLocator()
yearsFmt = DateFormatter('%Y')
fig, axis = pyplot.subplots()
axis.plot_date(x, y, '-')
axis.xaxis.set_major_locator(years)
axis.xaxis.set_major_formatter(yearsFmt)
axis.xaxis.set_minor_locator(months)
axis.autoscale_view()
axis.fmt_xdata = DateFormatter('%Y-%m-%d')
axis.fmt_ydate = lambda y: '{.2f}%'.format(y)
fig.autofmt_xdate()
xlbl = cols[0]['label']
ylbl = cols[1]['label']
pyplot.title('"{}" search frequency'.format(ylbl))
pyplot.xlabel(xlbl)
pyplot.ylabel(ylbl)
pyplot.show()
