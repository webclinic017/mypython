import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime
def get_stock_data(start_time,end_time,*stocklist):
    if not stocklist:return {}
    data_dict={}
    for i  in stocklist:
        data1 = yf.download(i,start_time,end_time)
        data_dict[i]=data1
    return data_dict
def get_next_event(*stocklist):
    if not stocklist: return {}
    data_next_ear_data={}
    for i in stocklist:
        temp = yf.Ticker(i)
        data_next_ear_data[i]=temp.calendar.loc['Earnings Date'].tolist()[0]
    return data_next_ear_data
def get_data(days):
    cur=datetime.date.today()
    delta=datetime.timedelta(days=days)
    return str(cur-delta)

def get_date_delta(str1,str2):
    date_time_obj1 = datetime.datetime.strptime(str1, '%Y-%m-%d')
    date_time_obj2 = datetime.datetime.strptime(str2, '%Y-%m-%d')
    return int(str(date_time_obj1-date_time_obj2).split()[0])

def get_options_data(date_str,cp="call",*stocklist):
    if not stocklist: return {}
    data_options={}
    for i in stocklist:
        temp=yf.Ticker(i)
        if cp=="put":data_options[i]=temp.option_chain(date_str).puts
        else:data_options[i]=temp.option_chain(date_str).calls
    return data_options


#def kelly_caculation():
    #return invest_percentage

if __name__ == "__main__":
    pass