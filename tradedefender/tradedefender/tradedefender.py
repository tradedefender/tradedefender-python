#!/usr/bin/env python3
import requests
import json


BASE_URL = "https://api.tradedefender.com/companies"


def strip_option_symbol(symbol):
    outSymbol = ""
    if(symbol is not False):
        for s in symbol:
            if(s.isdigit()):
                break
            else:
                outSymbol = outSymbol + s
        return(outSymbol)
    else:
        return("False")


def parameterize(host, params):
    url = host
    if(params["api_key"] is not False):
        url = host + "?api_key=" + str(params["api_key"])
        del params["api_key"]

    for p in params:
        if(params[p] is not False):
            url = url + "&" + p + "=" + params[p]

    return(url)


def make_request(url):
    response = json.loads(requests.get(url).text)
    return(response)


def companies(app_key=False, symbol=False, order_by=False, columns=False):
    host = BASE_URL
    if(symbol is not False):
        host = BASE_URL + "/" + symbol
    params = {"api_key": app_key,
              "order_by": order_by,
              "columns": columns}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def sicpeers(app_key=False, symbol=False, order_by=False, columns=False):
    host = BASE_URL + "/" + str(symbol) + "/sic-peers"
    params = {"api_key": app_key,
              "order_by": order_by,
              "columns": columns}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def stockprice(app_key=False, symbol=False):
    host = BASE_URL + "/" + str(symbol) + "/price"
    params = {"api_key": app_key}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def histpricedata(app_key=False, symbol=False, start_date=False,
                  end_date=False, order_by=False, columns=False):
    host = BASE_URL + "/" + str(symbol) + "/hist-price-data"
    params = {"api_key": app_key,
              "start_date": start_date,
              "end_date": end_date,
              "order_by": order_by,
              "columns": columns}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def histestimates(app_key=False, symbol=False, start_date=False,
                  end_date=False, order_by=False, columns=False):
    host = BASE_URL + "/" + str(symbol) + "/hist-earnings-and-estimates"
    params = {"api_key": app_key,
              "start_date": start_date,
              "end_date": end_date,
              "order_by": order_by,
              "columns": columns}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def balancesheets(app_key=False, symbol=False, start_date=False,
                  end_date=False, order_by=False, columns=False,
                  period_type=False):
    host = BASE_URL + "/" + str(symbol) + "/hist-balance-sheets"
    params = {"api_key": app_key,
              "start_date": start_date,
              "end_date": end_date,
              "order_by": order_by,
              "columns": columns,
              "period_type": period_type}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def cashflowstatements(app_key=False, symbol=False, start_date=False,
                       end_date=False, order_by=False, columns=False,
                       period_type=False):
    host = BASE_URL + "/" + str(symbol) + "/hist-cash-flow-statements"
    params = {"api_key": app_key,
              "start_date": start_date,
              "end_date": end_date,
              "order_by": order_by,
              "columns": columns,
              "period_type": period_type}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def incomestatements(app_key=False, symbol=False, start_date=False,
                     end_date=False, order_by=False, columns=False,
                     period_type=False):
    host = BASE_URL + "/" + str(symbol) + "/hist-income-statements"
    params = {"api_key": app_key,
              "start_date": start_date,
              "end_date": end_date,
              "order_by": order_by,
              "columns": columns,
              "period_type": period_type}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def optionchain(app_key=False, symbol=False, start_date=False,
                end_date=False, option_type=False, columns=False):
    host = BASE_URL + "/" + str(symbol) + "/options"
    params = {"api_key": app_key,
              "start_date": start_date,
              "type": option_type,
              "end_date": end_date,
              "columns": columns}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)


def option(app_key=False, symbol=False, columns=False):
    option_symbol = symbol
    symbol = strip_option_symbol(option_symbol)
    host = BASE_URL + "/" + str(symbol) + "/options/" + str(option_symbol)
    params = {"api_key": app_key,
              "columns": columns}
    request_url = parameterize(host, params)
    response = make_request(request_url)
    return(response)
