import yfinance as yfinance

#fghv is find high volume dates

def fghv(symbol, period ="1d", interval= "1d" )
    
#fetch historical data
    
data = yfinance.download("^ES", period= "1d",interval= "1d" )

#calculate average volume

avgvol = data['Volume'].mean()

#find dates where volume is above average by specified multiple
#hvd = high volume dates


hvd = data[data['Volume'] >= avgvol * 4].index

symbol = "^ES"

hvd = fghv(symbol)


