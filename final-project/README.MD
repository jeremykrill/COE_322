# Final Project Documentation

This is my final project for COE 332. The system is a web app that interfaces with a time-series dataset based on this [assignment](https://coe-332-sp21.readthedocs.io/en/main/homework/final_project.html). The dataset here is the daily returns of all S&P 500 constituents from the bottom of the COVID-19 crash (on March 23, 2020) to April 30, 2021. Essentially, the motivation here is to compare returns across different stocks, sectors, company sizes, and relative valuations. This identifying data is stored in a modified version of the ticker for a given company. For example, Apple Inc. would be stored as "AAPL-TECH-LARGE-GRO" to signify that it's in the information technology sector, is relatively large compared to other S&P 500 companies, and is a "growth" stock (in that its EV/EBITDA multiple is on the higher end). An important note here is that since the motivation of this project is to compare COVID-era returns across different company/stock factors, prices are given as the theoretical growth of $100 placed into a specific stock from 3/27/2020 to 4/30/2021, and that growth is based on the actual reported daily returns.

The user interfaces with the Redis database server via a Flask server, and implements a worker that reads jobs from a queue. The jobs in this case are plots of the returns over a given time period. It deploys over a test and prod environment, depending on the user/developer's needs. The corresponding Kubernetes deployments for these environemtns are contained in the k8s directory. Meanwhile, the app directory contains the source files for supporting the system, the docker directory contains the necessary Dockerfiles for the api and the worker images, and the data directory contains the datafiles. Below are corresponding deployment and user documentations. May your stonks only go up!

## Deployment ##

First, deploy the redis service, and make sure the pvc is deployed as well
```bash
[krilljs@isp02 test]$ kubectl apply -f krilljs-final-test-redis-pvc.yml
[krilljs@isp02 test]$ kubectl apply -f krilljs-final-test-redis-service.yml
```

Next, get the redis IP address, and enter it in the jobs.py file
```bash
[krilljs@isp02 test]$ kubectl get services -o wide
[krilljs@isp02 app]$ vim jobs.py
```

After the redis services are up and running, and we've accordingly adjusted jobs.py, our next step is to build the Docker images and push to Dockerhub. We use the following commands:
```bash
[krilljs@isp02 app]$ docker build -f krilljs/COE_332/final-project/docker/Dockerfile.api krilljs/final-project-api:1.0 .
[krilljs@isp02 app]$ docker build -f krilljs/COE_332/final-project/docker/Dockerfile.worker krilljs/final-project-worker:1.0 .
[krilljs@isp02 app]$ docker push krilljs/final-project-api:1.0
[krilljs@isp02 app]$ docker push krilljs/final-project-worker:1.0
```

In the k8s yaml files, make sure the image version selections are correct. Then, in the test directory, finish deploying k8s:
```bash
[krilljs@isp02 test]$ kubectl apply -f krilljs-final-test-redis-deployment.yml
[krilljs@isp02 test]$ kubectl apply -f krilljs-final-test-flask-deployment.yml
[krilljs@isp02 test]$ kubectl apply -f krilljs-final-test-flask-service.yml
[krilljs@isp02 test]$ kubectl apply -f krilljs-final-test-worker-deployment.yml
```

Make sure everything's running as planned. Repeat in the prod directory, replace "test" with "prod" as necessary above.

## User ##
Deploy the pythonDebug deployment to start playing with the system:
```bash
[krilljs@isp02 test]$ kubectl apply -f krilljs-pythonDebug-deployment.yml
```

Record the IP address for the flask service so we can curl into it:
```bash
[krilljs@isp02 test]$ kubectl get services
```

Then, exec into the pythonDebug pod and curl into the flask service, using port 5000
```bash
curl <ip-address>:5000/<route>
```

### Overview Of Functionality ###
Keys:
'ticker': The corresponding ticker for the publicly traded S&P 500 company
'sector': The corresponding GICS Sector name
'size': The relative size of the stock compared to mean of other S&P 500 constituents (either LARGE or SMALL)
'valuation': The relative valuation of the stock compared to the median of other S&P 500 constituents (either VAL, for a "value" stock, or GRO, for a "growth" stock)

1) Delete 
Arguments:
'db': Clears the redis database
'jobs': Clears currents jobs from redis
'images': Clears images from redis
'all': Clears keys from reids
'period': Clears entries from a specified time period
'date': Clears entries from a specified date

You use the following example command to delete all data:
```bash
curl '<flask-ip>:5000/delete/all'
```

2) Read
Arguments:
'all': Gets all data for specified keys
'returns': Gets returns for specified keys for given date range


You use the following example command to get data for a date range:
```bash
curl '<flask-ip>:5000/get/date?ticker=AAPL&sector=n&size=n&valuation=n&d1='3/27/2020'&d2='5/10/2020'
```
Note that since this system hasn't yet implemented the full functionality to view more than one field at a time, all but one entry should be set to 'n'.

3) Update
You use the following example command to update data:
```bash
curl '<flask-ip>:5000/update?stock=AAPL&sector=TECH&size=LARGE&valuation=GRO&date='3/27/2020'&price=61.35'
```

4) Create
You use the following example command to create a new dataset:
```bash
curl -X POST -H "content-type: application/json" -d '{"stock": "AAPL-TECH-LARGE-GRO", "price": {"4/09/2020": 66.37, "2/26/21": "121.05"}}' <flask-ip>:5000/create
```

5) Jobs
You can use the following example command to plot an image:
```bash
curl -X POST -H "content-type: application/json" -d '{"stocks": ["ticker": "TICKER", "sector": "SECTOR", "size": "SIZE", "valuation": "VALUATION"}, {<another stock>}], "date_range": [date1, date2]}' <flask-ip>:<flask-port>/graph
```

