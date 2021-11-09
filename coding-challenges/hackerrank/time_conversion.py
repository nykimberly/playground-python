"""
Given a time in 12-hour AM/PM format, convert to military (24-hour) time.

Inputs:
s: string - 12 hour format '12:01:00AM'

Outputs:
string - 24 hour format '00:01:00'

Approach: 
12h time pts: 12am, 1am, 12p, 1pm
24h time pts: 0, 1, 12, 13
Compute hours from 0 for 12h, and that is the 24h time
    if it is 12am, 0hrs, 1am 1hrs, 12pm, 12hrs, 1pm 13hrs
"""
def timeConversion(s: str) -> str:
    ampm = s[-2:]
    hour_str, minute_str, second_str = s[:-2].split(":")
    hour = int(hour_str)
    hours = hour % 12 + 12 if ampm == "PM" else hour % 12
    return "%.2d:%s:%s" % (hours, minute_str, second_str)


def timeConversionDT(s: str) -> str:
    from datetime import datetime
    dt = datetime.strptime(s, "%I:%M:%S%p")
    return datetime.strftime(dt, "%H:%M:%S")


if __name__ == "__main__":
    print(timeConversionDT("12:45:54AM"))
    print(timeConversionDT("12:45:54PM"))
    print(timeConversionDT("04:45:54PM"))
    print("Done!")
