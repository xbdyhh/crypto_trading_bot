import ftx

def wrap_ticker(ticker):
    if ticker['name']=='ftx':
        return ftx.wrap_ftx_ticker(ticker)