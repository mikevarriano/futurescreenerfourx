import yfinance as yfinance

#fghv is find high volume dates

def fghv(symbol, period ="1d", interval= "1d", vm= 4 )
    
#fetch historical data
    
data = yfinance.download(symbol, period= period,interval= interval )

#calculate average volume

avgvol = data['Volume'].mean()

#find dates where volume is above average by specified multiple
#hvd = high volume dates

