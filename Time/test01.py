from datetime import datetime, timedelta


# input args
s1 = '10:11:09'
s2 = '10:11:12'
ts = datetime.strptime(s1, '%H:%M:%S')
te = datetime.strptime(s2, '%H:%M:%S')

time = 0
while te > ts:
    if len({ts.hour, ts.minute, ts.second}) == 2:
        time += 1
        print(ts.time())
    ts += timedelta(seconds=1)

print(time)