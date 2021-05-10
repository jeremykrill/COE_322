# worker.py
from jobs import q, rd, update_job_status, get_job_data, add_image
from returns import return_keys
import datetime
import json
import matplotlib.pyplot as p

# Format data
def reformat(datum, data):
    if datum in data:
        return datum
    else:
        return "n"    

@q.worker
def plot(jid):
    update_job_status(jid, 'in progress')
    job_data = get_job_data(jid)

    dates = json.loads(job_data['dates'])
    # make sure dates are input correctly
    d1 = datetime.datetime(dates[0])
    d2 = datetime.datetime(dates[1]) 
    days = abs((d2 - d1).days)

    # Get keys
    keys = []
    stocks = json.loads(job_data['stocks'])
    for data in stocks: 

        ticker = reformat("ticker", data)
        sector = reformat("sector", data)
        size = reformat("size", data)
        valuation = reformat("valuation", data))

        k = return_keys(ticker,sector,size,valuation)
        for key in k:
            keys.append(key)

    for key in keys:
        values = []
        total_days = []
        for day in days:
            value = rd.hget(key,day)
            values.append(float(value))
            total_days.append(datetime.datetime(value)
            
        plt.plot(total_days, values, '-o', label = key)

    plt.xlabel('Date')
    plt.ylabel('Growth of $100')
    plt.legend()
    plt.show()

    plt.savefig('/plot.png')

    with open('/plot,png', 'rb') as f:
        pic = f.read()

    add_image(jid, pic)
    update_job_status(jid, 'complete')

    # Ah, need to clear the figure when done
    plt.clf()

plot()
