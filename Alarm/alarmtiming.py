from datetime import datetime
from playsound import playsound
import winsound

alarm_date = input('Enter the date on which you want to set the alarm (DD): ').strip()
alarm_time = ''.join(input("Enter the time of alarm to be set in HH:MM,AM/PM format: ").split())
music_or_beep = input("Enter m for a music or b for beep sound: ")
if music_or_beep == 'b':
    dur = int(input("Duration in seconds: ")) * 1000  # winsound needs ms
    freq = int(input("Frequency of the noise: "))

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_period = alarm_time[6:8].upper()

print('Setting alarm...')

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime('%I')
    current_minute = current_time.strftime('%M')
    current_period = current_time.strftime('%p')
    current_date = current_time.strftime('%d')
    if current_date == alarm_date and current_period == alarm_period and current_hour == alarm_hour and current_minute == alarm_minute:
        print('*' * 10)
        print('| Wake up! |')
        print('*' * 10)
        if music_or_beep == 'm':
            playsound('audio.wav')  # make sure audio.wav exists in your project folder
        else:
            winsound.Beep(freq, dur)
        break
