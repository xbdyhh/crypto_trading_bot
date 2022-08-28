def wrap_ftx_ticker(ticker):
    ticker['high']=ticker['info']['priceHigh24h']
    ticker['low'] = ticker['info']['priceLow24h']
    return ticker