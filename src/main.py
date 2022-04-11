def add_time(start_time, duration, day = None):
    hours = start_time.split()[0].split(":")[0]
    minutes = start_time.split()[0].split(":")[1]
    dur_hours = duration.split()[0].split(":")[0]
    dur_minutes = duration.split()[0].split(":")[1]
    period = start_time.split()[1]
    res_period = period
    days_passed = 0
    if day != None:
        week = {
                "monday": 1,
                "tuesday": 2,
                "wednesday": 3,
                "thurday": 4,
                "friday": 5,
                "saturday": 6,
                "sunday": 7
                }
        rev_week = {
                1: "monday",
                2: "tuesday",
                3: "wednesday",
                4: "thursday",
                5: "friday",
                6: "saturday",
                7: "sunday"
                }
        day = week.get(day.lower())
    if period.lower() == "pm":
        res_hours = int(hours) + 12
    else:
        res_hours = int(hours)
    res_minutes = int(minutes) + int(dur_minutes)
    while res_minutes >= 60:
        res_minutes -= 60
        res_hours += 1
    res_hours += int(dur_hours)
    while (res_hours > 24) or (res_hours == 24 and res_minutes > 0):
        days_passed += 1
        res_hours -= 24
    if res_hours > 12:
        res_period = "PM"
        res_hours -= 12
    elif res_hours == 12 and res_minutes > 0:
        res_period = "PM"
    elif res_hours == 0:
        res_period = "AM"
        res_hours += 12
    elif res_hours < 12:
        res_period = "AM"
    if res_minutes < 10:
        res_minutes = str(res_minutes)
        res_minutes = "0" + res_minutes
    if days_passed == 1:
        if day != None:
            day += 1
            day = rev_week.get(day)
            res_time = ":".join([str(res_hours), str(res_minutes)])
            days_passed = "(next day)"
            res_period += ","
            new_time = " ".join([res_time, res_period, day.capitalize(), days_passed])
            return new_time
        else:
            res_time = ":".join([str(res_hours), str(res_minutes)])
            days_passed = "(next day)"
            new_time = " ".join([res_time, res_period, days_passed])
            return new_time
    elif days_passed > 1:
        if day != None:
            day = (days_passed + day) % 7
            day = rev_week.get(day)
            res_period += ","
            res_time = ":".join([str(res_hours), str(res_minutes)])
            days_passed = "(" + str(days_passed)
            days_passed += " days later)"
            new_time = " ".join([res_time, res_period, day.capitalize(), days_passed])
            return new_time
        else:
            res_time = ":".join([str(res_hours), str(res_minutes)])
            days_passed = "(" + str(days_passed)
            days_passed += " days later)"
            new_time = " ".join([res_time, res_period, days_passed])
            return new_time
    else:
        if day != None:
            day = rev_week.get(day)
            res_period += ","
            res_time = ":".join([str(res_hours), str(res_minutes)])
            new_time = " ".join([res_time, res_period, day.capitalize()])
            return new_time
        else:
            res_time = ":".join([str(res_hours), str(res_minutes)])
            new_time = " ".join([res_time, res_period])
            return new_time


