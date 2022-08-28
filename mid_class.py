import time
import tool.tool as tool

class mid_class():
    # 初始化所需要的信息，如交易所密钥信息、初始化账户信息等
    # 其中exchange是cctx中实现了exchange class的库
    def __init__(self,exchange):
        exchange.load_markets()
        self.exchange = exchange
        self.init_timestamp = time.time()
        self.name = self.exchange.name
        self.id = exchange.id
        self
    def get_balance(self):
        self.Balance='___'
        self.Used='___'
        self.Free ='___'
        try:
            if self.exchange.has['fetchBalance']:
                self.Balance = self.exchange.fetch_balance()
            else:
                return False
            self.Used = self.Balance['used']
            self.Free = self.Balance['free']
            self.Balance = self.Balance['info']['result']
            return True
        except:
            return False

    def get_ticker(self,symbol):
        self.High = '___'
        self.Low = '___'
        self.Sell = '___'
        self.Last = '___'
        self.Bid = '___'
        self.Ask = '___'
        self.Volume = '___'
        try:
            self.ticker = self.exchange.fetch_ticker(symbol)
            self.ticker = tool.wrap_ticker(self.ticker)
            self.Low = self.ticker['low']
            self.High = self.ticker['high']
            self.Bid = self.ticker['low']
            self.Ask = self.ticker['ask']
            self.Volume=self.ticker['volume']
            return True
        except:
            return False

    def get_depth(self):
        pass
    def get_ohlc_data(self):
        #获取k线信息
        pass
    def create_order(self):
        pass
    def cancel_order(self):
        pass
