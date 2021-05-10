# api.py
from flask import Flask, request, jsonify
import json
from jobs import add_job, rd, j, image #check names
from data import get_keys #check names

app = Flask(__name__)

# Clear database
@app.route('delete/db')
def delete_db():
    for key in rd.keys():
       rd.delete(key)
    
    with open('data/spy_returns_daily.json','r') as f:
        data = json.load(f)

    for key in data:
        rd.hmset(key, data[key])

@app.route('delete/jobs')
def delete_jobs():
    for key in j.keys():
        j.delete(key)

# check name
@app.route('delete/images')
def delete_images():
    for key in image.keys():
        image.delete(key)

@app.route('delete/all', methods=['GET'])
def delete_all():
    ticker = str(request.args.get('ticker'))
    sector = str(request.args.get('sector'))
    size = str(request.args.get('size'))
    valuation = str(request.args.get('valuation'))

    keys = get_keys(ticker, sector, size, valuation)
    for key in keys:
        rd.delete(key)

@app.route('delete/period', methods=['GET'])
def delete_date():
    ticker = str(request.args.get('ticker'))
    sector = str(request.args.get('sector'))
    size = str(request.args.get('size'))
    valuation = str(request.args.get('valuation'))
    d1 = str(request.args.get('d1'))
    d2 = str(request.args.get('d2'))

    d1 = datetime.datetime(d1)
    d2 = datetime.datetime(d2)
    
    keys = get_keys(ticker, sector, size, valuation)
    for key in keys:
        for day in (d2 - d1).days
        rd.hdel(key, day)

@app.route('delete/date')
    ticker = str(request.args.get('ticker'))
    sector = str(request.args.get('sector'))
    size = str(request.args.get('size'))
    valuation = str(request.args.get('valuation'))
    d1 = str(request.args.get('d1'))

    keys = get_keys(ticker,sector,size,valuation)
    for key in keys:
        rd.hdel(key, year)

@app.route('/get/all', methods=['GET'])
def get_all():
    #inputs must be uppercase
    ticker = str(request.args.get('ticker'))
    sector = str(request.args.get('sector'))
    size = str(request.args.get('size'))
    valuation = str(request.args.get('valuation'))

    keys = get_keys(ticker,sector,size,valuation)
    l = []
    for key in keys:
        list[key] = rd.hgetall(key)

    return l

# gets the average returns of specified group of stocks
# over the given date range
@app.route('/get/returns', methods=['GET'])
def get_returns()
    ticker = str(request.args.get('ticker'))
    sector = str(request.args.get('sector'))
    size = str(request.args.get('size'))
    valuation = str(request.args.get('valuation'))
    d1 - str(request.args.get('d1'))
    d2 = str(request.args.get('d2'))

    d1 = datetime.datetime(d1)
    d2 = datetime.datetime(d2)
    
    keys = get_keys(ticker,sector,size,valuation)
    totreturns = []
    for key in keys:
        price1 = float(rd.hget(key,d1))
        price2 = float(rd.hget(key,d2))
        returns = float((price2 - price1)/price1)
        totreturns.append(returns)
    
    avg_returns = 0
    tot = 0
    count = 0
    for r in totreturns:
        count += 1
        tot += r
    avg_returns = r / count
    
    return 100*avg_returns

@app.route('/update', methods=['GET'])
def update()
    ticker = str(request.args.get('ticker'))
    sector = str(request.args.get('sector'))
    size = str(request.args.get('size'))
    valuation = str(request.args.get('valuation'))
    day = str(request.args.get('d1'))
    price =  str(request.args.get('price'))

    key = get_keys(ticker,sector,size,valuation)[0]
    rd.hset(key, day, price)

@app.route('/plot', methods=['GET','POST'])
def create_plot():
    job = request.get_json()
    stocks = json.dumps(job['stocks'])
    dates = json.dumps(job['dates'])
    add_job(stocks,dates)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
