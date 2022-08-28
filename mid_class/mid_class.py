import time


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

    def get_ticker(self):
        pass
    def get_depth(self):
        pass
    def get_ohlc_data(self):
        #获取k线信息
        pass
    def create_order(self):
        pass
    def cancel_order(self):
        pass
