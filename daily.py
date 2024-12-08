import yfinance as yf
import pandas_ta as ta
import csv


file_path="./FIPASCAN.csv"


upTrendStockList=[]
downTrendStockList=[]
valuZoneStocklist=[]
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        ticker = row[0]  
        # print(ticker)
        # ticker = "CARERATING.NS"
        df = yf.download(ticker, period="1y",interval='1d',progress=False)  # Adjust the period as needed

        # Calculate SuperTrend
        df = ta.supertrend(high=df['High'], low=df['Low'], close=df['Close'], period=9, multiplier=2)
        # # Print the DataFrame with SuperTrend

        supertrend2=df.tail(1)['SUPERT_7_2.0'].values[0]

        st2=int(supertrend2)

        df2 = yf.download(ticker, period="1y",interval='1d',progress=False)  # Adjust the period as needed
        df2 = ta.supertrend(high=df2['High'], low=df2['Low'], close=df2['Close'], period=9, multiplier=1.5)
        supertrend1point5=df2.tail(1)['SUPERT_7_1.5'].values[0]
        st1point5=int(supertrend1point5)
      
        tickerData = yf.Ticker(ticker)
        todayData = tickerData.history(period='1d')
        cmp=int(todayData['Close'].values[0])
        supertrenddifference=(st1point5-st2)*100/st2
        
        # print(ticker,',',supertrenddifference)
        

        if(cmp>st2 and cmp > st1point5):
            diff= cmp-st2
            diffper= round((diff/st2)*100,2)
            ticker.replace('.NS','')
            upTrendStockList.append(ticker.replace('.NS',',')+str(diffper))
            # print(ticker+" In Uptrend")


        if(cmp< st2 and cmp > st1point5):
            valuZoneStocklist.append(ticker.replace('.NS',''))
            # print("In VALUE Zone ")

        
        if(cmp< st2 and cmp < st1point5):
          diff= cmp-st2
          diffper= round((diff/st2)*100,2)
          ticker.replace('.NS','')
          downTrendStockList.append(ticker.replace('.NS',',')+str(diffper))
        #  print(ticker+"In decline Zone")



print("********** UpTrendStocks ***********",end='\n\n\n')

for uts in upTrendStockList:
        print(uts)

print("*********** DownTrendStocks ***********",end='\n\n\n')
for dts in downTrendStockList:
        print(dts)

print("********** ValueZoneStocks ***********",end='\n\n\n')
for vzs in valuZoneStocklist:
        print(vzs)
        