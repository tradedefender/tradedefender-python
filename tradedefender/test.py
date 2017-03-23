#!/usr/bin/env python3
import sys
import json
import datetime
import tradedefender

def execute_test(api_key):
    today = datetime.datetime.now()
    beforeToday = today - datetime.timedelta(days=500)
    afterToday = today + datetime.timedelta(days=500)
    today = today.strftime("%Y-%m-%d")
    beforeToday = beforeToday.strftime("%Y-%m-%d")
    afterToday = afterToday.strftime("%Y-%m-%d")

    testResults =   {"companies":"clean",
                    "sicpeers":"clean",
                    "stockprice":"clean",
                    "histpricedata":"clean",
                    "histestimates":"clean",
                    "balancesheets":"clean",
                    "cashflowstatements":"clean",
                    "incomestatements":"clean",
                    "optionchain":"clean",
                    "option":"clean"}
    #companies
    result = tradedefender.companies(app_key=api_key, symbol="AAPL", order_by="asc", columns="ticker,company_name,company_name_2,exchange,sec_cik")
    if("errors" in result):
        testResults["companies"] = result

    #sicpeers
    result = tradedefender.sicpeers(app_key=api_key, symbol="AAPL", order_by="asc", columns="ticker,company_name,company_name_2,exchange,sec_cik")
    if("errors" in result):
        testResults["sicpeers"] = result

    #stockprice
    result = tradedefender.stockprice(app_key=api_key, symbol="AAPL")
    if("errors" in result):
        testResults["stockprice"] = result

    #histpricedata
    result = tradedefender.histpricedata(app_key=api_key, symbol="AAPL", start_date=beforeToday, end_date=today, order_by="asc", columns="date,adjusted_close")
    if("errors" in result):
        testResults["histpricedata"] = result

    #histestimates
    result = tradedefender.histestimates(app_key=api_key, symbol="AAPL", start_date=beforeToday, end_date=today, order_by="asc", columns="date_announced,eps_act")
    if("errors" in result):
        testResults["histestimates"] = result

    #balancesheets
    result = tradedefender.balancesheets(app_key=api_key, symbol="AAPL", start_date=beforeToday, end_date=today, order_by="asc", columns="per_end_date", period_type="Q")
    if("errors" in result):
        testResults["balancesheets"] = result

    #cashflowstatements
    result = tradedefender.incomestatements(app_key=api_key, symbol="AAPL", start_date=beforeToday, end_date=today, order_by="asc", columns="per_end_date", period_type="Q")
    if("errors" in result):
        testResults["incomestatements"] = result

    #incomestatements
    result = tradedefender.cashflowstatements(app_key=api_key, symbol="AAPL", start_date=beforeToday, end_date=today, order_by="asc", columns="per_end_date", period_type="Q")
    if("errors" in result):
        testResults["cashflowstatements"] = result

    #optionchain
    result = tradedefender.optionchain(app_key=api_key, symbol="AAPL", start_date=today, end_date=afterToday, option_type="calls", columns="symbol,strike_price,delta,gamma,theta")
    option_symbol = ""
    if("errors" in result):
        testResults["optionchain"] = result
    else:
        option_symbol = result["data"][0]["calls"][0]["symbol"]

    #option
    result = tradedefender.option(app_key=api_key, symbol=option_symbol, columns="strike_price,delta,gamma,theta")
    if("errors" in result):
        testResults["option"] = result

    return(testResults)

if __name__ == "__main__":
    if(sys.version_info[0]>=3):
        api_key = input("Enter App Key: ")
    else:
        api_key = raw_input("Enter App Key: ")

    print(execute_test(api_key))
