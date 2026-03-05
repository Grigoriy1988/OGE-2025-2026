from datetime import datetime

time1 = datetime.strptime("18:30", "%H:%M")
time2 = datetime.strptime("14:45", "%H:%M")

if time1 < time2:
    print("time1 раньше time2")
elif time1 > time2:
    print("time1 позже time2")
else:
    print("Времена равны")
