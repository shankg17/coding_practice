import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import time
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
    def nextValidId(self, orderId):
        self.reqAccountSummary(1, "All", "NetLiquidation")  # 'NetLiquidation' is the total account value
    def accountSummary(self, reqId, account, tag, value, currency):
        if tag == "NetLiquidation":
            print(f"Account value: {account} {value} {currency}")
app = TestApp()
app.connect("127.0.0.1", 7496, 0)
print(app.isConnected())
app.run()
app.disconnect()


