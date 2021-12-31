import yahoo_fin
from yahoo_fin.stock_info import *
from yahoo_fin.stock_info import get_analysts_info #analyst methods
from yahoo_fin import news #New modudule with single function get_yf_rss	
from yahoo_fin.options import get_options_chain #for options methods
from yahoo_fin import options#for options methods

# import pandas as pd
# import matplotlib.pyplot as mp


#===============================
#Header, inlcude when using module
#===============================
heads = {'Host': 'www.sec.gov', 'Connection': 'close',
         'Accept': 'application/json, text/javascript, */*; q=0.01', 'X-Requested-With': 'XMLHttpRequest',
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
         }

stock = 'ASX'


#===============================
# Stock Methods
#===============================
analysts_info = get_analysts_info(stock)
balancesheet = get_balance_sheet(stock, yearly=True)
company_info=get_company_info(stock)
company_officers=get_company_officers(stock)
currencies=get_currencies()
get_data= (get_data(stock, start_date='2021-12-01', end_date=None, index_as_date=False, interval="1d"))
day_gainers=get_day_gainers()
day_losers=get_day_losers()
most_active=get_day_most_active
dividends=get_dividends(stock,start_date='2021-12-01', end_date=None, index_as_date=False)
earnings=get_earnings(stock)
earnings_for_date=get_earnings_for_date('2021-12-23')
earnings_history=get_earnings_history(stock)
earn_in_day_range=get_earnings_in_date_range('2021-12-01','2021-12-23')
financials=get_financials(stock, yearly=True,quarterly=True) #pulls incomestatement, balancesheet, yearly cashflow
futures=get_futures()
holders=get_holders(stock)
income_statement=get_income_statement(stock,yearly=True)
live_price=get_live_price(stock)
market_status=get_market_status()
# next_earnings_date=get_next_earnings_date(stock) #something is broke in this method
# premarket_price=get_premarket_price(stock)
# postmarket_price=get_postmarket_price(stock)
quote_data=get_quote_data(stock)
quote_table=get_quote_table(stock,dict_result=True)  #pulls a good amount of fields
splits=get_splits(stock)
stats=get_stats(stock)
stats_valuation=get_stats_valuation(stock)
# top_crypto=get_top_crypto(stock)
undervalued_large_caps=get_undervalued_large_caps()
# # dow=tickers_dow(include_company_data=False)
# ftse100=tickers_ftse100(include_company_data=False)
# ftse250=tickers_ftse250(include_company_data=False)
# nasdaq=tickers_nasdaq(include_company_data=False)
# nifty50=tickers_nifty50(include_company_data=False)
# niftybank=tickers_niftybank()
# other_stocks=tickers_other(include_company_data=False)
# sp500=tickers_sp500(include_company_data=False)
print(quote_table)


# #===============================
# #Options
# #===============================
# option_calls=get_calls(stock,date=None)
# option_expiration_dates=get_expiration_dates(stock)
# options_chains=get_options_chain(stock,date=None)
# option_puts=get_puts(stock,date=None)

#===============================
#Yahoo News
#===============================
from yahoo_fin import news
 
data=news.get_yf_rss("nflx")
# print(data.shape)
# fig,ax=mp.subplots()

# # for x in stocklist:
# #     # print(get_earnings_history(x))
# # #     print(get_earnings(x))
# # #    # print(get_market_status(x))
# # #     print(get_analysts_info(x))
# #     # print(get_company_info(x[0]))
# df = (get_data(stock, start_date='2021-12-01',end_date=None, index_as_date=False, interval="1d"))
# df.plot(x="date", y=["high","close","low"], kind="line", figsize=(10,9))
# # mp.show
# ax.plot = (df['close'], df['date'])
# mp.show
# print (df['volume'], df['close'])
# print(df.head())
# print(df.columns)

# # print(df.shape)
# # print(df.rows)
# mp.show
