# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a
# boolean indicating if we are on vacation, return a string of the form "7:00"
# indicating when the alarm clock should ring.
#
# Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
# Unless we are on vacation -- then on weekdays it should be "10:00" and
# weekends it should be "off".

day = 0
on_vacation = True

if on_vacation:
    if day == 0 or day == 6:
        print("off")
    else:
        print("10:00")
else:
    if day == 0 or day == 6:
        print("10:00")
    else:
        print("07:00")


# You can condense this further!
is_weekend = day == 0 or day == 6

if on_vacation and is_weekend:
    print("off")
elif on_vacation or is_weekend:
    print("10:00")
else:
    print("07:00")
