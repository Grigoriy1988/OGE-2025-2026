import datetime as dt

start = input().split(':')
stop = input().split(':')
h = dt.timedelta(minutes=int(input()))
start_t = dt.timedelta(hours=int(start[0]), minutes=int(start[1]))
stop_t = dt.timedelta(hours=int(stop[0]), minutes=int(stop[1]))
while start_t < stop_t:
    d = stop_t - start_t
    print(f'There are {int(d.total_seconds() // 60)} of minutes left.')
    start_t += h
print('WAKE UP!')
