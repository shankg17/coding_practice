# Let's import the libraries
import yfinance as yf 
# Pandas is used for dataframe and tabular data manipulation
import pandas as pd 


#Creating a function to execute DCF Model
def dfcf_fn(stock):
    fc = int((stock.get_cash_flow().iloc[0,0]))
    dfcf_acc = 0
    fcf_acc = 0
    g_10 = float(input("Enter Growth Rate for upto 10 Years(in %):"))
    g_11 = float(input("Enter Growth Rate for >10 Years(in %):"))
    disc_rate = float(input("Enter Discount Rate(in %):"))

    for i in range(1,11):
        fcf = float(fc*(1+(g_10/100))**i)
        #print(fcf)
        fcf_11 = fcf*((1+(g_11/100))/((disc_rate-g_11)/100))
        dfcf= round(float(fcf/((1+(disc_rate/100))**i)),2)
        #print(dfcf)
        dfcf_acc = dfcf + dfcf_acc
   
    dfcf_total = dfcf_acc + (fcf_11/(1+(disc_rate/100))**10)
    print('Valuation w/o MOS(in B):{}'.format(round(dfcf_total/1000000000),1))
    print('Current MCAP(in B):{}'.format(round(stock.fast_info['marketCap']/1000000000),1))
    return round(dfcf_total/1000000000,2)

#Code for Stock Valuation Data Frame for multiple stocks:

stock_valuation_df = pd.DataFrame(columns=['symbol','comp_name','intrinsic_value','mkt_cap'])
tick = str(input('Input Ticker Symbol:'))
stock = yf.Ticker(tick.upper())
shares = stock.fast_info['marketCap']/stock.info['currentPrice']
print(stock.info['shortName'])
print("Current Price",stock.info['currentPrice'])
#stock.get_cash_flow()
print("Free Cash Flow",stock.get_cash_flow().iloc[0,0]/1000000)

q = [stock,stock.info['shortName'], dfcf_fn(stock),round(stock.fast_info['marketCap']/1000000000,2)]

stock_valuation_df.loc[len(stock_valuation_df)] = q #This is how we append a list to a DF.
print("Buy Price:",round(((q[2]*1000000000)/shares),2))
stock_valuation_df