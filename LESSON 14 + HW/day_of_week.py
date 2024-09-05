# DAY OF THE WEEK

# START

def day_of_week(day: int) -> str:
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    if day not in days:
        raise ValueError("Invalid day number")
    return days[day]

# END