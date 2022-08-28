import ccxt

# 你可以将ftx换成任何你需要的交易所
if __name__ == '__main__':
    ftx = ccxt.ftx({
        'proxies': {
            'http': 'http://localhost:7890',
            'https': 'http://localhost:7890',
        },
    })
    ftx.apiKey='your api key'
    ftx.secret='your api secret'