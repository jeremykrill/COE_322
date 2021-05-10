# returns.py
from jobs import rd

def _stock_name(input):
""" Returns all keys matching "input"
    "input" can be the ticker, ticker + sector, 
    ticker + sector + size, or
    ticker + sector + size + valuation
"""
    keys = []
    for key in rd.keys():
        if key[0:len(input)] == input:
            keys.append(key)
    
    return keys

def _stock_sector(input):
""" Returns all keys matching the inputted sector
    "input" can be the sector, sector + size, or
    sector + size + valuation
"""
    keys = []
    start = 0
    for key in rd.keys():
    # Since tickers differ in length, we search
    # until we find the first "-"
        start = key.find("-",1,5)
        if key[start:start+len(input)] == input:
            keys.append(key)

    return keys

def _stock_size(input):
""" Returns all keys matching the inputted size
    "input" can be the size or size + valuation
"""
    keys = []
    start = 0
    for key in rd.keys():
    # Since tickers differ in length, we search
    # until we find the first "-"
    # Since the rest of the stock's data has 
    # a standard length, we can hardcode now
        start = key.find("-",1,5)
        if key[start+6:start+6+len(input)] == input:
            keys.append(key)

    return keys

def _stock_valuation(input):
""" Returns all keys matching inputted valuation
    "input" is the valuation of the stock, either
    a "value" stock, or a "growth" stock
"""
keys = []
    start = 0
    for key in rd.keys():
    # Since tickers differ in length, we search
    # until we find the first "-"
    # Since the rest of the stock's data has
    # a standard length, we can hardcode now
        start = key.find("-",1,5)
        if key[start+12:start+12+len(input)] == input:
            keys.append(key)

    return keys

def return_keys(ticker, sector, size, valuation):
""" Returns all keys based on ther ticker, sector, size, and valuation
    Trying to do all 15 possible combinations of ticker, sector, size,
    and valuation would take too many if-else statements for the scope
    of this project. So, to simplify things, users should only input a 
    ticker, sector, size, or valuation entry, and make everything else
    'n' as their entry.
"""
    if ticker != "n":
        keys = _stock_ticker(ticker)
    elif sector != "n":
        keys = _stock_sector(sector)
    elif size != "n":
        keys = _stock_size(size)
    elif valuation != "n":
        keys = _stock_valuation(valuation)
    else
        raise Exception
    return keys
