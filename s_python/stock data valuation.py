# Let's import the library
import yfinance as yf 
# Pandas is used for dataframe and tabular data manipulation
import pandas as pd
# Investpy package to pull stock market data from Investing.com 
import investpy as invpy


symbols = ['^GSPC','^IXIC','^RUT','^VIX',
           '^GSPTSE','^NSEI',
           'DX-Y.NYB','CAD=X','CADINR=X','INR=X',
          '^IRX','^TNX']
daily_fin_data_df = pd.DataFrame(columns=['symbol','name','cmp','change%','day_range','52W_range'])
for i in symbols:
    stock = yf.Ticker(i)
    q = [i,stock.info['longName'], f'{stock.info['regularMarketPrice']:,}',
         round(stock.info['regularMarketChangePercent'],2), stock.info['regularMarketDayRange'], 
         stock.info['fiftyTwoWeekRange']]
    #print(q)
    daily_fin_data_df.loc[len(daily_fin_data_df)] = q 

daily_fin_data_df



#invpy.get_bond_historical_data(bond = 'Canada 2Y', from_date= '05/01/2025', to_date = '02/02/2025')
#"US10YT=X"

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime
# Time range

# Import the data from FRED
yields = ['DGS3MO', 'DGS10']
df_yields = pdr.DataReader(yields, 'fred')
df_yields.tail(5)


# yfinance is an open-source tool used to get market data from Yahoo 
# Let's install the library
#!pip3 install yfinance

# Let's import the library
import yfinance as yf 

# Pandas is used for dataframe and tabular data manipulation
import pandas as pd 

# Investpy package to pull stock market data from Investing.com 
import investpy as invpy

# Very useful library to imp0rt data from many sources- https://thecleverprogrammer.com/2021/03/22/pandas-datareader-using-python-tutorial/
import pandas_datareader as pdr

#pd.options.display.max_rows = 999
#f'{10000000:,}'   #To use comma format for numbers.


tick = str(input('Input Ticker Symbol:'))
stock = yf.Ticker(tick.upper())
stock.info['displayName']
#stock.get_cash_flow()

## Code for DFCF Calculation

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


## Function for DFCF Calculation

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
    
    dfcf_fn(stock)


    #Function for stock data fetching:

def stock_data_fn(stock):
    cf_table = stock.cashflow
    bs_table = stock.balancesheet
    pl_table = stock.financials

    symbol = stock.info['symbol']
    comp_name = stock.info['shortName']
    market = stock.info['market']
    exchange = stock.info['exchange']
    currency = stock.info['currency']
    mktcap_B = round(stock.info['marketCap']/1000000000,2)
    cmp = stock.info['currentPrice']
    sector = stock.info['sector']
    industry = stock.info['industry']

#Income
    revenue_B = round(stock.info['totalRevenue']/1000000000,2)
    gross_profit_B = round(stock.info['grossProfits']/1000000000,2)
    gross_margin = round(stock.info['grossMargins']*100,2)
    operating_margin = round(stock.info['operatingMargins']*100,2)
    netprofit_margin = round(stock.info['profitMargins']*100,2)

#print(stock.info[''])

    operating_exp_B = round(pl_table.loc['Operating Expense'].iloc[0]/1000000000,2)
    operating_inc_B = round(pl_table.loc['Operating Income'].iloc[0]/1000000000,2)
    tax_B = round(pl_table.loc['Tax Provision'].iloc[0]/1000000000,2)
    net_profit_B = round(pl_table.loc['Net Income'].iloc[0]/1000000000,2)
#pl_table.loc[''].iloc[0]

#B/S
    cash_B = round(stock.info['totalCash']//1000000000,2)
#stock.info['']
    outstanding_shares = stock.info['sharesOutstanding']

    ret_earning_B = round(bs_table.loc['Retained Earnings'].iloc[0]//1000000000,2)
    total_assets_B = round(bs_table.loc['Total Assets'].iloc[0]/1000000000,2)
    total_liab_B = round(bs_table.loc['Total Liabilities Net Minority Interest'].iloc[0]/1000000000,2)
    tota_eq_B = round(bs_table.loc['Total Equity Gross Minority Interest'].iloc[0]/1000000000,2)
    debt_long_B = round(bs_table.loc['Long Term Debt'].iloc[0]/1000000000,2)
    current_assets_B = round(bs_table.loc['Current Assets'].iloc[0]/1000000000,2)
    current_liab_B = round(bs_table.loc['Current Liabilities'].iloc[0]/1000000000,2)
    payable_B = round(bs_table.loc['Accounts Payable'].iloc[0]/1000000000,2)
    receivable_B = round(bs_table.loc['Accounts Receivable'].iloc[0]/1000000000,2)
    ppe_B = round(bs_table.loc['Net PPE'].iloc[0]/1000000000,2)
    #inventory_B = round(bs_table.loc['Inventory'].iloc[0]/1000000000,2)
#bs_table.loc[''].iloc[0]
#bs_table.loc[''].iloc[0]



#CF

    cfo_B = round(cf_table.loc['Operating Cash Flow'].iloc[0]/1000000000,2)
    fcf_B = round(cf_table.loc['Free Cash Flow'].iloc[0]/1000000000,2)

    div_paid_B = round(cf_table.loc['Cash Dividends Paid'].iloc[0]/1000000000,2)
    depreciation_B = round(cf_table.loc['Depreciation Amortization Depletion'].iloc[0]/1000000000,2)
    debt_issued_B = round(cf_table.loc['Net Long Term Debt Issuance'].iloc[0]/1000000000,2)
    stock_issued_B = round(cf_table.loc['Net Common Stock Issuance'].iloc[0]/1000000000,2)
    cff_B = round(cf_table.loc['Financing Cash Flow'].iloc[0]/1000000000,2)
    cfi_B = round(cf_table.loc['Investing Cash Flow'].iloc[0]/1000000000,2)
    cap_expenditure_B = round(cf_table.loc['Capital Expenditure'].iloc[0]/1000000000,2)

#Ratio

    roe = round(stock.info['returnOnEquity']*100,2)
    roa = round(stock.info['returnOnAssets']*100,2)
    debt2eq = round(stock.info['debtToEquity']/100,2)
    pb = stock.info['priceToBook']

    quick_ratio = stock.info['quickRatio']
    current_ratio = stock.info['currentRatio']
    pe_forward = stock.info['forwardPE']
    div_payout_ratio = round(stock.info['payoutRatio']*100,2)
    div_yield = stock.info['dividendYield']
    peg_trailing = stock.info['trailingPegRatio']

#stock.info['']
#stock.info['']

#Others:
    low_52w = stock.info['fiftyTwoWeekLow']
    high_52w =stock.info['fiftyTwoWeekHigh']
    beta = stock.info['beta']
#stock.info['']
    stock_data = [symbol, comp_name, market, exchange,currency, sector, industry, cmp, mktcap_B,
                 cfo_B, cap_expenditure_B]
    
    print(stock_data)
    return stock_data


#Code for stock data for multiple tickers at the same time:
stock_data_df = pd.DataFrame(columns=['symbol','comp_name','market','exchange','currency','sector',
                                       'industry','cmp','mktcap_B','cfo_B','cap_expenditure_B'])


#print(stock_data_df)
tickers = ['AAPL','OXY','CNR.TO','COST','CP.TO','SPGI','CBOE','TSM']
for i in tickers:
    tick = str(i)
    stock = yf.Ticker(tick.upper())
    #print(stock)
    p = stock_data_fn(stock)
    stock_data_df.loc[len(stock_data_df)] = p #This is how we append a list to a DF.

print(stock_data_df)

# Code for stock data

cf_table = stock.cashflow
bs_table = stock.balancesheet
pl_table = stock.financials

symbol = stock.info['symbol']
comp_name = stock.info['shortName']
market = stock.info['market']
exchange = stock.info['exchange']
currency = stock.info['currency']
mktcap_B = stock.info['marketCap']/1000000000
cmp = stock.info['currentPrice']
sector = stock.info['sector']
industry = stock.info['industry']

#Income
revenue_B = stock.info['totalRevenue']/1000000000
gross_profit_B = stock.info['grossProfits']/1000000000
gross_margin = stock.info['grossMargins']*100
operating_margin = stock.info['operatingMargins']*100
netprofit_margin = stock.info['profitMargins']*100

#print(stock.info[''])

operating_exp_B = pl_table.loc['Operating Expense'].iloc[0]/1000000000
operating_inc_B = pl_table.loc['Operating Income'].iloc[0]/1000000000
tax_B = pl_table.loc['Tax Provision'].iloc[0]/1000000000
net_profit_B = pl_table.loc['Net Income'].iloc[0]/1000000000
#pl_table.loc[''].iloc[0]

#B/S
cash_B = stock.info['totalCash']//1000000000
#stock.info['']
outstanding_shares = stock.info['sharesOutstanding']

ret_earning_B = bs_table.loc['Retained Earnings'].iloc[0]//1000000000
total_assets_B = bs_table.loc['Total Assets'].iloc[0]/1000000000
total_liab_B = bs_table.loc['Total Liabilities Net Minority Interest'].iloc[0]/1000000000
tota_eq_B = bs_table.loc['Total Equity Gross Minority Interest'].iloc[0]/1000000000
debt_long_B = bs_table.loc['Long Term Debt'].iloc[0]/1000000000
current_assets_B = bs_table.loc['Current Assets'].iloc[0]/1000000000
current_liab_B = bs_table.loc['Current Liabilities'].iloc[0]/1000000000
payable_B = bs_table.loc['Accounts Payable'].iloc[0]/1000000000
receivable_B = bs_table.loc['Accounts Receivable'].iloc[0]/1000000000
ppe_B = bs_table.loc['Net PPE'].iloc[0]/1000000000
inventory_B = bs_table.loc['Inventory'].iloc[0]/1000000000
#bs_table.loc[''].iloc[0]
#bs_table.loc[''].iloc[0]



#CF

cfo_B = stock.info['operatingCashflow']/1000000000
fcf_B = stock.info['freeCashflow']/1000000000

div_paid_B = cf_table.loc['Cash Dividends Paid'].iloc[0]/1000000000
depreciation_B = cf_table.loc['Depreciation Amortization Depletion'].iloc[0]/1000000000
debt_issued_B = cf_table.loc['Net Long Term Debt Issuance'].iloc[0]/1000000000
stock_issued_B = cf_table.loc['Net Common Stock Issuance'].iloc[0]/1000000000
cff_B = cf_table.loc['Financing Cash Flow'].iloc[0]/1000000000
cfi_B = cf_table.loc['Investing Cash Flow'].iloc[0]/1000000000
cap_expenditure_B = cf_table.loc['Capital Expenditure'].iloc[0]/1000000000

#Ratio

roe = stock.info['returnOnEquity']*100
roa = stock.info['returnOnAssets']*100
debt2eq = stock.info['debtToEquity']
pb = stock.info['priceToBook']

quick_ratio = stock.info['quickRatio']
current_ratio = stock.info['currentRatio']
pe_forward = stock.info['forwardPE']
div_payout_ratio = stock.info['payoutRatio']*100
div_yield = stock.info['dividendYield']
peg_trailing = stock.info['trailingPegRatio']

#stock.info['']
#stock.info['']

#Others:
low_52w = stock.info['fiftyTwoWeekLow']
high_52w =stock.info['fiftyTwoWeekHigh']
beta = stock.info['beta']
#stock.info['']


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

# Code to export the data frame into a csv file.
gfg_csv_data = stock_valuation_df.to_csv('Stocks Valuation DF_py.csv', index = True)

#stock_valuation_df.drop(5, inplace = True) # To drop a row by index.
#stock_valuation_df

import pandas as pd

API_KEY = 'BM5SMITEZIGZK3PT'

csv_url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={API_KEY}"

# Read the returned CSV of listed stocks/ETFs
symbols_df = pd.read_csv(csv_url)

print(symbols_df.head())

symbols_df.to_csv('output.csv', index=False)

import pandas as pd
sym_df = pd.read_excel('C:/Users/array/Documents/iCloudDrive/Documents/Programming/Python Projects/Listed Companies in NASDAQ.xlsx')
listedcompanies_df = pd.DataFrame(columns=['symbol','mcap'])
for i in sym_df['symbol']:
    ticker = yf.Ticker(i)
    market_cap = ticker.info.get('marketCap')
    if market_cap is not None:
        entry = [ticker, market_cap / 1000000]
        listedcompanies_df.loc[len(listedcompanies_df)] = entry
    else:
        entry = [ticker, "Market cap not available"]
        listedcompanies_df.loc[len(listedcompanies_df)] = entry
        
listedcompanies_df