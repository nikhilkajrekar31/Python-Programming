# Name: Nikhil Kajrekar
# UTA ID: 1001552488

time = float(input("Input time in seconds: "))
time1 = int(time)
day = time // (24 * 3600)
time %= (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

if time1 >= 60 and time1 < 3600:
    print("Minutes: ",minutes)
    print("Seconds: ",seconds)
elif time1 >= 3600 and time1 < 86400:
    print("Hours: ", hour)
    print("Minutes: ", minutes)
    print("Seconds: ", seconds)
else:
    print("Days: ", day)
    print("Hours: ", hour)
    print("Minutes: ", minutes)
    print("Seconds: ", seconds)


