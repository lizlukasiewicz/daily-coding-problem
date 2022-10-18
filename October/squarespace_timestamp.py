"""
This problem was asked by Postmates.

The “active time” of a courier is the time between the pickup and dropoff of a delivery. 
Given a set of data formatted like the following:

(delivery id, timestamp, pickup/dropoff)
Calculate the total active time in seconds. A courier can pick up multiple orders before dropping them off. The timestamp is in unix epoch seconds.

For example, if the input is the following:

(1, 1573280047, 'pickup')
(1, 1570320725, 'dropoff')
(2, 1570321092, 'pickup')
(3, 1570321212, 'pickup')
(3, 1570322352, 'dropoff')
(2, 1570323012, 'dropoff')
The total active time would be 1260 seconds.

"""
import datetime
import time

def deliveries(input):
    active_time=0
    deliveries={}
    for data in input:
        #print(f'timestamp:{datetime.datetime.fromtimestamp(data[1])}')
        if data[0] in deliveries and data[2]=='dropoff':
            print(f'pickup: {datetime.datetime.fromtimestamp(deliveries[data[0]][0])} dropoff: {datetime.datetime.fromtimestamp(data[1])}')
            sec=abs(data[1]-deliveries[data[0]][0])
            print(f'{sec//60} min')
            active_time+=sec
        else:
            deliveries[data[0]] = [data[1], data[2]]
    print(f'active: {active_time} ')

test=[
    (1, 1573280047, 'pickup'),
    (1, 1570320725, 'dropoff'),
    (2, 1570321092, 'pickup'),
    (3, 1570321212, 'pickup'),
    (3, 1570322352, 'dropoff'),
    (2, 1570323012, 'dropoff')
]
deliveries(test)