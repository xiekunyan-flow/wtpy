import config, csv
import calendar
import wget
import os
from binance.client import Client
import datetime

client = Client(config.API_KEY, config.API_SECRET)

cyear = 2022
cmonth = 1
nyear = 2023
nmonth : 4

def timestamp_to_formatted_string(timestamp):
    # 将时间戳转换为datetime对象
    dt_object = datetime.datetime.fromtimestamp(timestamp)

    # 将datetime对象格式化为所需的字符串
    formatted_string = dt_object.strftime("%Y/%m/%d,%H:%M:%S")
    date_part = formatted_string[:10]  # 提取前10个字符，即年月日部分
    time_part = formatted_string[11:]  # 提取从第11个字符到末尾的部分，即小时分钟秒部分

    return date_part,time_part

# print(timestamp_to_formatted_string(1546300806260/1000))

def get_data(symbol, byear, bmonth, bday, eyear, emonth, eday, period):
    filename = symbol + '-' + str(byear) + str(bmonth).zfill(2) + str(bday).zfill(2) + '-' + str(eyear) + str(emonth).zfill(2) + str(eday).zfill(2) + '-' + period + '.csv'
    print("csv is:", filename)

    file_path = os.path.dirname(__file__)
    os.chdir(file_path)

    if not os.path.exists(os.path.join(file_path, 'cand')):
        os.makedirs(os.path.join(file_path, 'cand'))

    with open(os.path.join('cand',filename), 'w', newline='') as csvfile:
        candlestick_writer = candlestick_writer = csv.writer(csvfile)

        stDate = str(bday).zfill(2) + " " + calendar.month_abbr[bmonth] + ", " + str(byear)
        endDate = str(eday).zfill(2) + " " + calendar.month_abbr[emonth] + ", " + str(eyear)
        print("start time is:", stDate, " end time is:", endDate)
        candlesticks = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, stDate, endDate)

        print(len(candlesticks))

        candlestick_writer.writerow(["<Date>", "<Time>", "<Open>", "<High>", "<Low>", "<Close>", "<Volume>"])
        for candlestick in candlesticks:
            date,time = timestamp_to_formatted_string(candlestick[0] / 1000)
            open_price = candlestick[1]
            high_price = candlestick[2]
            low_price = candlestick[3]
            close_price = candlestick[4]
            volume = candlestick[5]
            candlestick_writer.writerow([date,time, open_price, high_price, low_price, close_price, volume])

        csvfile.close()

# while cyear >= 2017:
#     if cmonth + 3 > 12:
#         nyear = cyear +1
#         nmonth = 1
#     else :
#         nyear = cyear
#         nmonth = cmonth + 3
#     get_data("BTCUSDT",cyear,cmonth,1,nyear,nmonth,1,Client.KLINE_INTERVAL_1MINUTE)
    
#     if cmonth > 1:
#         cmonth -= 3
#     else :
#         cyear -= 1
#         cmonth = 10

get_data("BTCUSDT",2023,7,1,2023,7,2,Client.KLINE_INTERVAL_1MINUTE)

url = 'https://data.binance.vision/data/spot/monthly/trades/BTCUSDT/BTCUSDT-aggTrades-2023-01.zip'
url = 'https://data.binance.vision/data/spot/monthly/trades/BNBUSDT/BNBUSDT-trades-2019-01.zip'
url = 'https://data.binance.vision/data/spot/monthly/aggTrades/BNBUSDT/BNBUSDT-aggTrades-2019-01.zip'
url = 'https://data.binance.vision/data/spot/monthly/aggTrades/BNBUSDT/BNBUSDT-aggTrades-2020-01.zip'
url = 'https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1s/BTCUSDT-1s-2023-01.zip'
# file_name = wget.download(url)
# print(file_name)