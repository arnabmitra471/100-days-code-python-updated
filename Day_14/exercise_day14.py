import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)

timestamp = int(time.strftime("%H"))

if timestamp >= 6 and timestamp < 12:
    print("Good morning")
elif timestamp >= 12 and timestamp < 16:
    print("Good Afternoon")
elif timestamp >= 16 and timestamp <= 20:
    print("Good evening")
else:
    print("Good Night")