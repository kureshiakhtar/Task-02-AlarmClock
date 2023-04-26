import datetime
# -------------------------------Alarm Clockk-----------------------------------#

from playsound import playsound
alarmHour = int(input("Enter Hour : "))
alarmMin = int(input("Enter Minutes : "))
alarmAm = input("am / pm : ")

if alarmAm == "pm":
    alarmHour += 12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print("playing..")
        playsound(
            "F:/software engg/Python/Python InternPe/Project/01 AlarmClock/Alarm.mp3")
        break
